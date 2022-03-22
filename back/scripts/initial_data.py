import sys

sys.path.insert(0, "")


from src.domain.mountain import MountainRepository, Mountain


database_path = "data/database.db"


# Users


# Contacts

teide = Mountain(name="Teide", height=3715)
pagasarri = Mountain(name="Pagasarri", height=750)

mountain_repository = MountainRepository(database_path)
mountain_repository.save(teide)
mountain_repository.save(pagasarri)


print("Base de datos inicializada en " + database_path)
