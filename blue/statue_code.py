from hashlib import md5

from werkzeug.http import generate_etag, is_resource_modified
from flask import Blueprint, request, make_response, render_template

blue_statue_code = Blueprint("blue_statue_code", __name__)


@blue_statue_code.route(rule="/")
def statue_code():
    return make_response(render_template("statuecode.html"))


@blue_statue_code.route(rule="cache_age.html")
def statue_code_cache_age():
    resp = make_response(render_template("cache.html", word="Age Test!"))
    resp.cache_control.public = True
    resp.cache_control.max_age = 31536000
    return resp


etags, times = ["孙悟空", "孙悟空", "唐三藏"], 0


@blue_statue_code.route(rule="cache_etag.html")
def statue_code_cache_etag():
    global times
    resp = make_response(render_template("cache.html", word="Etag Test! " + etags[times % len(etags)]))
    times += 1
    resp.cache_control.public = True

    # resp_etag = md5(resp.data).hexdigest()
    # if "If-None-Match" in request.headers and request.headers["If-None-Match"] == resp_etag:
    #     return resp.data, 304
    # else:
    #     resp.headers["ETag"] = resp_etag
    #     return resp

    resp_etag = generate_etag(resp.data)
    # is_resource_modified(request.environ, etag=resp_etag, data=resp.data)
    if is_resource_modified(request.environ, data=resp.data):
        resp.headers["ETag"] = resp_etag
        return resp
    else:
        return resp.data, 304
