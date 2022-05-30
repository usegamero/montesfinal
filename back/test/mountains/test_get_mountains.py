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
    )

    mountain_repository.save(teide)

    pagasarri = Mountain(
        2,
        "Pagasarri",
        750,
        "Bilbao",
        "https://st4.depositphotos.com/2117021/20370/i/450/depositphotos_203704608-stock-photo-pagasarri-mountain-peak-bilbao.jpg",
        "Vizcaya",
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
        },
        {
            "id": 2,
            "name": "Pagasarri",
            "height": 750,
            "city": "Bilbao",
            "img": "https://st4.depositphotos.com/2117021/20370/i/450/depositphotos_203704608-stock-photo-pagasarri-mountain-peak-bilbao.jpg",
            "location": "Vizcaya",
        },
    ]
