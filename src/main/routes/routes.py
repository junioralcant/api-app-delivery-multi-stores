from flask import Blueprint, jsonify, request

from src.main.adapters.request_http_adapter import request_http_adapter
from src.main.factories.user_finder_controller_factory import (
    user_finder_controller_factory,
)
from src.main.factories.user_register_controller_factory import (
    user_register_controller_factory,
)

user_route_bp = Blueprint("user_route", __name__)


@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    response = request_http_adapter(request, user_finder_controller_factory())
    print("#################")
    print(response.body)
    return jsonify(response.body), response.status_code


@user_route_bp.route("/user", methods=["POST"])
def register_user():
    response = request_http_adapter(request, user_register_controller_factory())
    return jsonify(response.body), response.status_code
