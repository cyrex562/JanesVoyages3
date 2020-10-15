from flask import Blueprint, current_app, jsonify

bp = Blueprint('main', __name__, url_prefix='/api/v1')


@bp.route("/", methods=["GET"])
def default_route():
    return {"message": "API V1"}
