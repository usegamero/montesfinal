from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.mountain import MountainRepository, Mountain


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

    response = client.delete("/api/mountains/1")
    response_get = client.get("/api/mountains")
    assert response_get.json == []
