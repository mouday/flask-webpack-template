# -*- coding: utf-8 -*-

from flask_webpack_app.main import app

if __name__ == '__main__':
    app.debug = False
    app.run()
