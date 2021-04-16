# -*- coding: utf-8 -*-

from flask import Flask
from flask_controller import FlaskControllerRegister

from flask_webpack_app.flask_ext import WebpackFlaskStaticDigest

app = Flask(__name__)


# flask digest compile
WebpackFlaskStaticDigest(app)

# route rule
register = FlaskControllerRegister(app)
register.register_package('flask_webpack_app.controllers')
