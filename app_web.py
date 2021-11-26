from uuid import uuid4
from http.server import BaseHTTPRequestHandler

from flask import Flask, make_response, render_template, request, jsonify

from utils.config import ConfigFlask
from blue.js_encrypt import blue_js_encrypt
from blue.js_cookie import blue_js_cookie
from blue.statue_code import blue_statue_code
from blue.up_down import blue_up_down

if __name__ == "__main__":
    # 所有api请求json返回,格式{succ": True, "code": "0000", "msg": "成功", "data":dict}
    app = Flask(import_name="demo", template_folder="template", static_folder="static", static_url_path="/static")

    @app.route("/")
    def home():
        response = make_response(render_template("home.html"))
        response.set_cookie("tgc", str(uuid4()), path='', httponly=True)
        response.set_cookie("session", str(uuid4()), path='', httponly=False)
        return response

    app.register_blueprint(blue_js_encrypt, url_prefix="/js_encrypt")
    app.register_blueprint(blue_js_cookie, url_prefix="/js_cookie")
    app.register_blueprint(blue_statue_code, url_prefix="/statue_code")
    app.register_blueprint(blue_up_down, url_prefix="/up_down")
    app.config.from_object(ConfigFlask())
    print(app.url_map)
    BaseHTTPRequestHandler.protocol_version = "HTTP/1.1"
    app.run()