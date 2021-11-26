from flask import Blueprint, request, make_response, render_template

blue_js_cookie = Blueprint("blue_js_cookie", __name__)


@blue_js_cookie.route(rule="/")
def cookie():
    response = make_response(render_template("cookie.html"))
    response.set_cookie("channel", "cookie", path='', httponly=False)
    return response
