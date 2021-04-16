# -*- coding: utf-8 -*-
from flask_controller import FlaskController


class LoginController(FlaskController):
    def index(self):
        return 'Login index'
