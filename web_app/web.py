# -*- coding: utf-8 -*-
# --- author: wtavares
# --- Web Aplication

from flask import render_template


def home():
    """Home page handler"""

    return render_template('index.html')


def update():
    """Update the repo"""

    return render_template('index.html')



