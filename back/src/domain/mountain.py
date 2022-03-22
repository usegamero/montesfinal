import sqlite3


class Mountain:
    def __init__(self,name,height):
        self.name= name
        self.height = height
       

    def to_dict(self):
        return {
            "name": self.name,
            "height": self.height,
           
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
                name text,
                height integer
               
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

   

    def save(self, mountain):
        sql = """insert into mountains (name,height) values (
            :name,:height
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
