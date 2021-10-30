import os
from datetime import timedelta

os.environ.setdefault("FLASK_ENV", "development")


class ConfigFlask(object):
    # 环境变量
    ENV = None
    # debug模式的设置,开发环境用，自动重启项目，日志级别低，报错在前端显示具体代码
    DEBUG = None
    # 测试模式的设置，无限接近线上环境，不会重启项目，日志级别较高，不会在前端显示错误代码
    TESTING = False
    PROPAGATE_EXCEPTIONS = None
    PRESERVE_CONTEXT_ON_EXCEPTION = None
    # session秘钥配置 无状态
    SECRET_KEY = None
    # 主机名设置
    SERVER_NAME = None
    # 应用根目录配置
    APPLICATION_ROOT = "/"
    # 5M
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    # 15 分钟超时
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(minutes=15)

    TRAP_BAD_REQUEST_ERRORS = None
    TRAP_HTTP_EXCEPTIONS = False
    EXPLAIN_TEMPLATE_LOADING = False
    PREFERRED_URL_SCHEME = "http"
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    JSONIFY_PRETTYPRINT_REGULAR = False
    # 设置jsonify响应时返回的contentype类型
    JSONIFY_MIMETYPE = "application/json"
    TEMPLATES_AUTO_RELOAD = None
