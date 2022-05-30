import sys

sys.path.insert(0, "")


from src.domain.mountain import MountainRepository, Mountain


database_path = "data/database.db"


# Users


# Contacts

teide = Mountain(
    id=1,
    name="Teide",
    height=3715,
    city="Tenerife",
    img="https://st3.depositphotos.com/1465849/13457/i/450/depositphotos_134570400-stock-photo-teide-volcano-mountain.jpg",
    location="Islas Canarias",
)
pagasarri = Mountain(
    id=2,
    name="Pagasarri",
    height=750,
    city="Bilbao",
    img="https://st4.depositphotos.com/2117021/20370/i/450/depositphotos_203704608-stock-photo-pagasarri-mountain-peak-bilbao.jpg",
    location="Vizcaya",
)
aneto = Mountain(
    id=3,
    name="Aneto",
    height=3404,
    city="Benasque",
    location="Huesca",
    img="https://st3.depositphotos.com/31863598/34227/i/450/depositphotos_342278160-stock-photo-pico-aneto-pyrenees-huesca-aragon.jpg",
)
gorbea = Mountain(
    id=4,
    name="Gorbea",
    height=1482,
    city="Zeanuri",
    location="Vizcaya",
    img="https://st3.depositphotos.com/7670718/12651/i/450/depositphotos_126512826-stock-photo-autumn-sunrise-in-gorbea-natural.jpg",
)
amboto = Mountain(
    id=5,
    name="Amboto",
    height=750,
    city="Durango",
    location="Vizcaya",
    img="https://st2.depositphotos.com/2117021/6366/i/450/depositphotos_63663743-stock-photo-urkiola-sanctuary.jpg",
)

mountain_repository = MountainRepository(database_path)
mountain_repository.save(teide)
mountain_repository.save(pagasarri)
mountain_repository.save(aneto)
mountain_repository.save(gorbea)
mountain_repository.save(amboto)


print("Base de datos inicializada en " + database_path)
