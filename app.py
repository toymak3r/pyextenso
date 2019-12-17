#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pyextenso/app.py

import os
from flask import Flask, jsonify
from interpretador import Interpretador

app = Flask(__name__)


@app.route('/')
def root():
    result = {"result": "Bem vindo ao tradutor de numerais."}
    return jsonify(result)


@app.route('/<string:numero>')
@app.route('/<int:numero>')
def traduzir(numero):
    interpretador = Interpretador(tipo='json')
    return interpretador.extenso(numero)


@app.route('/dic/<string:dict>')
def dicionario(dict):
    interpretador = Interpretador(tipo='json')
    dicionario = interpretador.carregar_dicionario(dict)
    return dicionario


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host='0.0.0.0', port=port)
