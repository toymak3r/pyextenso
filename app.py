#!/usr/bin/env python
# -*- coding: latin-1 -*-
# certi_app/app.py

From flask import Flask
app = Flask(__name__)

@app.route('/')
def root:
    return "{ 'result': 'Bem vindo ao CERTI descritor de números' }"

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')

