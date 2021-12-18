from flask import Blueprint, request, make_response, render_template

blue_js_cookie = Blueprint("blue_js_cookie", __name__)


@blue_js_cookie.route(rule="/sub1")
def cookie1():
    response = make_response(render_template("cookie.html"))
    response.set_cookie("channel", "s1", path='/js_cookie/sub1', httponly=False)
    return response


@blue_js_cookie.route(rule="/sub2", methods=["POST"])
def cookie2():
    response = make_response("ok")
    response.set_cookie("channel", "s2", path='/js_cookie/sub2', httponly=False)
    return response