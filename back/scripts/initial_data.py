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
    description="El Teide es un volcán situado en la isla española de Tenerife, en Canarias. Cuenta con una altitud oficial de 3715 metros sobre el nivel del mar y 7500 metros sobre el lecho oceánico, siendo el pico más alto de España, el de cualquier tierra emergida del océano Atlántico y el tercer mayor volcán de la Tierra desde su base en el lecho oceánico, después del Mauna Kea y el Mauna Loa, ambos en Hawái. La altitud del Teide convierte además a la isla de Tenerife en la décima isla más alta del mundo.",
)
pagasarri = Mountain(
    id=2,
    name="Pagasarri",
    height=750,
    city="Bilbao",
    img="https://st4.depositphotos.com/2117021/20370/i/450/depositphotos_203704608-stock-photo-pagasarri-mountain-peak-bilbao.jpg",
    location="Vizcaya",
    description="El Pagasarri es una cima situada al sur de la villa de Bilbao, cuya altitud es de 671 m. Esta cumbre es en realidad una cima secundaria del monte Ganeta, aunque popularmente se le llama Pagasarri a toda la montaña, que forma parte del cinturón verde que rodea Bilbao, tanto por el N como por el S.",
)
aneto = Mountain(
    id=3,
    name="Aneto",
    height=3404,
    city="Benasque",
    location="Huesca",
    img="https://st3.depositphotos.com/31863598/34227/i/450/depositphotos_342278160-stock-photo-pico-aneto-pyrenees-huesca-aragon.jpg",
    description="El Aneto es el pico más elevado de los Pirineos, con una altitud de 3404 metros sobre el nivel del mar. Se encuentra situado en el Parque natural Posets-Maladeta, en el municipio español de Benasque, provincia de Huesca, comunidad autónoma de Aragón.",
)
gorbea = Mountain(
    id=4,
    name="Gorbea",
    height=1482,
    city="Zeanuri",
    location="Vizcaya",
    img="https://st3.depositphotos.com/7670718/12651/i/450/depositphotos_126512826-stock-photo-autumn-sunrise-in-gorbea-natural.jpg",
    description="El monte Gorbea es la cumbre más alta del macizo montañoso del mismo nombre, situado en los Montes Vascos, a caballo entre las provincias de Álava y Vizcaya, en el País Vasco.",
)
amboto = Mountain(
    id=5,
    name="Amboto",
    height=750,
    city="Durango",
    location="Vizcaya",
    img="https://st2.depositphotos.com/2117021/6366/i/450/depositphotos_63663743-stock-photo-urkiola-sanctuary.jpg",
    description="El Amboto es un monte entre Vizcaya y Álava en el País Vasco, de 1331 metros de altitud. Es uno de los montes más conocidos de los Montes Vascos por su importancia en la cultura tradicional vasca. En él la mitología vasca fija la morada principal de la diosa Mari, conocida como la Dama de Amboto.",
)

mountain_repository = MountainRepository(database_path)
mountain_repository.save(teide)
mountain_repository.save(pagasarri)
mountain_repository.save(aneto)
mountain_repository.save(gorbea)
mountain_repository.save(amboto)


print("Base de datos inicializada en " + database_path)
