from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.mountain import MountainRepository, Mountain


def test_end_point_should_return_mountains():
    mountain_repository = MountainRepository(temp_file())
    app = create_app(repositories={"mountain": mountain_repository})
    client = app.test_client()
    teide = Mountain("Teide", 3715)
    pagasarri = Mountain("Pagasarri", 750)
    mountain_repository.save(teide)
    mountain_repository.save(pagasarri)

    response = client.get("/api/mountains")

    assert response.json == [
        {"name": "Teide", "height": 3715},
        {"name": "Pagasarri", "height": 750},
    ]
