import sqlite3


class Mountain:
    def __init__(self, id, name, height, city, img, location):
        self.id = id
        self.name = name
        self.height = height
        self.city = city
        self.img = img
        self.location = location

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "city": self.city,
            "img": self.img,
            "location": self.location,
        }


class MountainRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists mountains (
                id INTEGER,
                name VARCHAR(100),
                height INTEGER,
                city VARCHAR(100),
                img varchar,
                location VARCHAR(100)
               
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def save(self, mountain):
        sql = """insert into mountains (id,name,height,city,img,location) values (
          :id,:name,:height,:city,:img,:location
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            mountain.to_dict(),
        )
        conn.commit()

    def get_all(self):
        sql = """select * from mountains"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        mountains = [Mountain(**item) for item in data]
        return mountains

    def get_by_id(self, id):
        sql = """SELECT * FROM mountains WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        data = cursor.fetchone()
        mountain = Mountain(**data)
        return mountain

    def delete_by_id(self, id):
        sql = """DELETE FROM mountains WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        print(sql, id)
        conn.commit()
