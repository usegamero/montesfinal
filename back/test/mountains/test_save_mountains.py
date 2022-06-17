from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.mountain import MountainRepository, Mountain


def test_should_save_mountain():

    # ARRANGE (given)

    mountain_repository = MountainRepository(temp_file())
    app = create_app(repositories={"mountain": mountain_repository})
    client = app.test_client()

    # ACT (when)
    body = {
        "id": 1,
        "name": "Teide",
        "height": 3715,
        "city": "Tenerife",
        "img": "https://st3.depositphotos.com/1465849/13457/i/450/depositphotos_134570400-stock-photo-teide-volcano-mountain.jpg",
        "location": "Islas Canarias",
        "description": "El Teide es un volcán situado en la isla española de Tenerife, en Canarias. Cuenta con una altitud oficial de 3715 metros sobre el nivel del mar y 7500 metros sobre el lecho oceánico, siendo el pico más alto de España, el de cualquier tierra emergida del océano Atlántico y el tercer mayor volcán de la Tierra desde su base en el lecho oceánico, después del Mauna Kea y el Mauna Loa, ambos en Hawái. La altitud del Teide convierte además a la isla de Tenerife en la décima isla más alta del mundo.",
    }
    response = client.post("/api/mountains", json=body)

    # ASSERT (then)

    assert response.status_code == 200

    response_get = client.get("/api/mountains/1")

    mountain = response_get.json
    assert mountain["id"] == 1
    assert mountain["name"] == "Teide"
    assert mountain["height"] == 3715
    assert mountain["city"] == "Tenerife"
    assert (
        mountain["img"]
        == "https://st3.depositphotos.com/1465849/13457/i/450/depositphotos_134570400-stock-photo-teide-volcano-mountain.jpg"
    )
    assert mountain["location"] == "Islas Canarias"
    assert (
        mountain["description"]
        == "El Teide es un volcán situado en la isla española de Tenerife, en Canarias. Cuenta con una altitud oficial de 3715 metros sobre el nivel del mar y 7500 metros sobre el lecho oceánico, siendo el pico más alto de España, el de cualquier tierra emergida del océano Atlántico y el tercer mayor volcán de la Tierra desde su base en el lecho oceánico, después del Mauna Kea y el Mauna Loa, ambos en Hawái. La altitud del Teide convierte además a la isla de Tenerife en la décima isla más alta del mundo."
    )
