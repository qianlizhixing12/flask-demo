from uuid import uuid4

from flask import Blueprint, request, make_response, render_template

blue_tcp = Blueprint("blue_tcp", __name__)


@blue_tcp.route(rule="/")
def tcp():
    return make_response(render_template("tcp.html"))


@blue_tcp.route(rule="tcp_connect.do")
def tcp_connect():
    # data = str(uuid4()) * 2000
    data = "--good--"
    return data, 200
