
# 自定义jinja2模板引擎环境
from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import  staticfiles_storage


def jinja2_environment(**options):
    # 1.创建jinja2环境
    env = Environment(**options)
    # 2.自定义相关的语法
    env.globals.update({
        'url': reverse,
        'static':staticfiles_storage
    }),
    return env