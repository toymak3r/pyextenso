#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import jsonify
import json


class Interpretador:

    limite_inferior = -99999
    limite_superior = 99999
    numero = 0
    dicionario = ""
    tipo = "json"                 # Default format

    def __init__(self, tipo="json", lang="ptbr"):
        if tipo is not None:
            self.tipo = tipo
        self.carregar_dicionario(lang)

    def carregar_dicionario(self, lang):
        arquivo_name = "{}.json".format(lang)
        try:
            arquivo = open(arquivo_name, "r")
            content = arquivo.read()
            self.dicionario = json.loads(content)
            arquivo.close()
            return self.formata_saida(self.dicionario)
        except:
            error = {"error": "Não foi possível \
                      abrir arquivo de dicionario: {} ".format(arquivo_name)}
            return self.formata_saida(error)

    def setar_limites(self, minimo, maximo):
        try:
            self.limite_inferior = int(minimo)
            self.limite_superior = int(maximo)
        except:
            error = {"error": "Parâmetro informado em formato incorreto.\
                                Deve ser inteiro."}
            return self.formata_saida(error)

    def formata_saida(self, resultado):
        if self.tipo == "json":
            return jsonify(resultado)

    def extenso(self, numeral):
        if numeral is None:
            return self.formata_saida("número não informado, parâmetro obrigatório")

        try:
            self.numero = int(numeral)
        except:
            error = {"error": "Parâmetro informado em formato incorreto"}
            return self.formata_saida(error)

        if self.numero >= self.limite_inferior and self.numero <= self.limite_superior:
            numero_string = str(self.numero)[::-1]
            grupo_numeros = {}
            grupo_extenso = []
            indice = 0
            remover_unidade = False

            while (len(numero_string) > 0):
                    grupo_numeros[indice] = numero_string[0:3]
                    numero_string = numero_string.replace(
                        grupo_numeros[indice], '', 1)
                    indice += 1

            for chave in grupo_numeros.keys():
                indice = 0
                negativo = None
                for numero in grupo_numeros[chave]:
                    indice_str = str(indice)
                    if numero == "-":
                        negativo = self.dicionario["numbers"]["specials"][numero]
                        grupo_numeros[chave] = grupo_numeros[chave].replace(
                            "-", "")
                    else:
                        if indice == 1 and numero == "1":
                            numero = numero + grupo_numeros[chave][indice - 1]
                            numero_extenso = self.dicionario["numbers"]["0"][numero]
                            remover_unidade = True
                        elif indice == 2 and numero == "1":
                            if grupo_numeros[chave][indice - 1] and grupo_numeros[chave][indice - 2] == "0":
                                numero_extenso = self.dicionario["numbers"]["specials"]["100"]
                            else:
                                numero_extenso = self.dicionario["numbers"][indice_str][numero]
                        else:
                            numero_extenso = self.dicionario["numbers"][indice_str][numero]

                        if numero != "0":
                            if chave > 0 and indice == 0:
                                complemento = self.dicionario["numbers"]["complementos"][str(
                                    chave)]
                                grupo_extenso.append(" "+complemento)
                            grupo_extenso.append(numero_extenso)
                        indice += 1

                print(grupo_extenso)
                print(grupo_numeros)

            if remover_unidade and grupo_extenso[0] != self.dicionario["numbers"]["0"]["10"]:
                del grupo_extenso[0]

            if remover_unidade and grupo_extenso[4] != self.dicionario["numbers"]["0"]["10"]:
                del grupo_extenso[3]

            extenso = ''
            contagem = len(grupo_extenso)

            if negativo:
                extenso += negativo+" "

            for palavra in grupo_extenso[::-1]:
                if contagem != len(grupo_extenso) and contagem != len(grupo_extenso) - 2:
                    extenso += " e "
                extenso += palavra
                contagem -= 1
            response = {"extenso": extenso}
            return self.formata_saida(response)
        else:
            error = {"error": "Limites permitidos: entre {} e {}"
                     .format(self.limite_inferior,
                             self.limite_superior)}
            return self.formata_saida(error)
