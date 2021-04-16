# -*- coding: utf-8 -*-
from flask_controller import FlaskController
from flask import render_template


class IndexController(FlaskController):
    def __init__(self):
        self.count = 0

    def index(self):
        self.count += 1
        return render_template('index.html', count=self.count)

    def login(self):
        return "login"
