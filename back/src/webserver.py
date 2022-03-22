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

    # @app.route("/api/info", methods=["GET"])
    # def info_get():
    #     info = repositories["info"].get_info()
    #     return object_to_json(info)

    # @app.route("/api/contacts", methods=["GET"])
    # def contacts_get_all_by_user():
    #     user_id = request.headers.get("Authorization")
    #     all_contacts = repositories["contacts"].search_by_user_id(user_id)
    #     return object_to_json(all_contacts)

    # @app.route("/api/contacts", methods=["POST"])
    # def contacts_post():
    #     body = request.json
    #     contact = Contact(**body)
    #     repositories["contacts"].save(contact)

    #     return ""

    # @app.route("/api/contacts/<id>", methods=["GET"])
    # def contacts_get_by_id(id):
    #     contact = repositories["contacts"].get_by_id(id)
    #     return object_to_json(contact)

    # @app.route("/api/users", methods=["GET"])
    # def users_get_all():
    #     all_users = repositories["users"].get_all()
    #     return object_to_json(all_users)

    return app
