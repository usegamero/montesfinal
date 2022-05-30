from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json

from src.domain.mountain import Mountain


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/mountains", methods=["GET"])
    def mountains_get():
        mountain = repositories["mountain"].get_all()

        return object_to_json(mountain)

    @app.route("/api/mountains/<id>", methods=["GET"])
    def mountains_get_by_id(id):
        mountain = repositories["mountain"].get_by_id(id)
        return object_to_json(mountain)

    @app.route("/api/mountains", methods=["POST"])
    def mountains_post():
        body = request.json
        mountain = Mountain(**body)
        repositories["mountain"].save(mountain)

        return ""

    @app.route("/api/mountains/<id>", methods=["DELETE"])
    def mountains_delete_by_id(id):
        repositories["mountain"].delete_by_id(id)
        return ""

    return app
