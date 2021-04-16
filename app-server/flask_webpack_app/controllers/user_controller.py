# -*- coding: utf-8 -*-
from flask_controller import FlaskController


class UserController(FlaskController):

    def user_name(self, name, age: int = 23):
        return 'username'

    def user(self, uid):
        return "uid" + uid
