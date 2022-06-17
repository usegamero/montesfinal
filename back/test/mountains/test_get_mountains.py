from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.mountain import MountainRepository, Mountain


def test_empty_data_base_should_not_return_mountains():
    mountain_repository = MountainRepository(temp_file())
    app = create_app(repositories={"mountain": mountain_repository})
    client = app.test_client()

    response = client.get("/api/mountains")

    assert response.json == []


def test_end_point_should_return_mountains():
    mountain_repository = MountainRepository(temp_file())
    app = create_app(repositories={"mountain": mountain_repository})
    client = app.test_client()

    teide = Mountain(
        1,
        "Teide",
        3715,
        "Tenerife",
        "https://st3.depositphotos.com/1465849/13457/i/450/depositphotos_134570400-stock-photo-teide-volcano-mountain.jpg",
        "Islas Canarias",
        "El Teide es un volcán situado en la isla española de Tenerife, en Canarias. Cuenta con una altitud oficial de 3715 metros sobre el nivel del mar y 7500 metros sobre el lecho oceánico, siendo el pico más alto de España, el de cualquier tierra emergida del océano Atlántico y el tercer mayor volcán de la Tierra desde su base en el lecho oceánico, después del Mauna Kea y el Mauna Loa, ambos en Hawái. La altitud del Teide convierte además a la isla de Tenerife en la décima isla más alta del mundo.",
    )

    mountain_repository.save(teide)

    pagasarri = Mountain(
        2,
        "Pagasarri",
        750,
        "Bilbao",
        "https://st4.depositphotos.com/2117021/20370/i/450/depositphotos_203704608-stock-photo-pagasarri-mountain-peak-bilbao.jpg",
        "Vizcaya",
        "El Pagasarri es una cima situada al sur de la villa de Bilbao, cuya altitud es de 671 m. Esta cumbre es en realidad una cima secundaria del monte Ganeta, aunque popularmente se le llama Pagasarri a toda la montaña, que forma parte del cinturón verde que rodea Bilbao, tanto por el N como por el S.",
    )
    mountain_repository.save(pagasarri)
    # -------------

    response = client.get("/api/mountains")

    assert response.json == [
        {
            "id": 1,
            "name": "Teide",
            "height": 3715,
            "city": "Tenerife",
            "img": "https://st3.depositphotos.com/1465849/13457/i/450/depositphotos_134570400-stock-photo-teide-volcano-mountain.jpg",
            "location": "Islas Canarias",
            "description": "El Teide es un volcán situado en la isla española de Tenerife, en Canarias. Cuenta con una altitud oficial de 3715 metros sobre el nivel del mar y 7500 metros sobre el lecho oceánico, siendo el pico más alto de España, el de cualquier tierra emergida del océano Atlántico y el tercer mayor volcán de la Tierra desde su base en el lecho oceánico, después del Mauna Kea y el Mauna Loa, ambos en Hawái. La altitud del Teide convierte además a la isla de Tenerife en la décima isla más alta del mundo.",
        },
        {
            "id": 2,
            "name": "Pagasarri",
            "height": 750,
            "city": "Bilbao",
            "img": "https://st4.depositphotos.com/2117021/20370/i/450/depositphotos_203704608-stock-photo-pagasarri-mountain-peak-bilbao.jpg",
            "location": "Vizcaya",
            "description": "El Pagasarri es una cima situada al sur de la villa de Bilbao, cuya altitud es de 671 m. Esta cumbre es en realidad una cima secundaria del monte Ganeta, aunque popularmente se le llama Pagasarri a toda la montaña, que forma parte del cinturón verde que rodea Bilbao, tanto por el N como por el S.",
        },
    ]
