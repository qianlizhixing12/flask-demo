from flask import Blueprint, jsonify, request, make_response, render_template, send_from_directory

blue_up_down = Blueprint("blue_up_down", __name__)


@blue_up_down.route(rule="/")
def up_down():
    return make_response(render_template("up_down.html"))


@blue_up_down.route(rule="img_download.do", methods=["POST"])
def img_download():
    return send_from_directory("img", "favicon.ico", as_attachment=True)