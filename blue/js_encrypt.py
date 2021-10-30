from flask import Blueprint, jsonify, request, make_response, render_template, send_from_directory

from utils.decorator import api_response
from data.user import get_users, get_users_map

blue_js_encrypt = Blueprint("blue_js_encrypt", __name__)


@blue_js_encrypt.route(rule="aes_hook.html")
def aes_hook_html():
    users = get_users()
    return make_response(render_template("aeshook.html", users=users))


@blue_js_encrypt.route(rule="aes_hook.do", methods=["GET", "POST"])
@api_response
def aes_hook():
    if request.method == "GET":
        user_id = request.args["user_id"]
    elif request.method == "POST":
        user_id = request.form["user_id"]
    users = get_users_map()
    return {"password": users[user_id]["password"]}
