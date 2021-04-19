# -*- coding: utf-8 -*-

from flask import Flask
from flask_controller import FlaskControllerRegister
from flask_static_digest import FlaskStaticDigest

app = Flask(__name__)

# flask digest compile
FlaskStaticDigest(app)

# route rule
register = FlaskControllerRegister(app)
register.register_package('flask_webpack_app.controllers')
