# -*- coding: utf-8 -*-

from app import app  # from app 指导入 app 包里的 __iniy__.py 所以这句话的含义是导入 __.init__.py 里面的 app实例


@app.route('/', methods=['GET'])
def index():
    return 'hello world, hello flask'
