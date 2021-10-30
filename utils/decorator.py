import json
import random

from flask import request, jsonify

from utils.aes import aes_cbc_pkcs7_encrypt, aes_cbc_pkcs7_decrypt, iv


def api_response(func):
    # data: dict, code: str = "0000", succ: bool = True, mag: str = "成功"
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            data, code, msg = result, "0000", "成功"
        elif isinstance(result, list):
            data, code, msg = result
        else:
            assert "返回非标准格式"

        if "encryptkey" in request.headers and code == "0000":
            # 转化key
            encryptkey_c = aes_cbc_pkcs7_decrypt(iv, request.headers["encryptkey"])
            encryptkey_c, encryptkey_s, mod = float(encryptkey_c), random.random(), ord("a") - ord("0")
            key = (str(encryptkey_c + encryptkey_s).replace(".", "") + "0000000000000000")[:16]
            key = "".join(map(lambda c: chr(mod + ord(c)), key))
            # 加密
            data = aes_cbc_pkcs7_encrypt(key, json.dumps(data))
            response = jsonify({"code": code, "msg": msg, "data": data})
            response.headers["encryptkey"] = encryptkey_s
        else:
            response = jsonify({"code": code, "msg": msg, "data": data})

        return response

    return wrap