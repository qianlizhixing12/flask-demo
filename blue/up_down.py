import os

from flask import Blueprint, jsonify, request, make_response, render_template, send_from_directory, url_for, redirect
from werkzeug.utils import secure_filename

blue_up_down = Blueprint("blue_up_down", __name__)


@blue_up_down.route(rule="/")
def up_down():
    return make_response(render_template("up_down.html"))


img_path = os.path.join(os.path.abspath(os.curdir), "img")


@blue_up_down.route(rule="img_download.do", methods=["POST"])
def img_download():
    filename = request.form["filename"]
    return send_from_directory(img_path, filename, as_attachment=True)


@blue_up_down.route(rule="img_upload.do", methods=["POST"])
def img_upload():
    f = request.files['filename']
    filename = secure_filename(f.filename)
    f.save(os.path.join(img_path, filename))
    return redirect(url_for('blue_up_down.up_down'))
