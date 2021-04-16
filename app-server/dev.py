# -*- coding: utf-8 -*-
from livereload import Server

from flask_webpack_app.main import app

# 静态文件热加载
app.config['FLASK_WEBPACK_DEV_HOST'] = 'http://localhost:8383'
app.debug = True

if __name__ == '__main__':

    print(app.url_map)

    live_server = Server(app.wsgi_app)
    live_server.watch("**/*.*")
    live_server.serve()
