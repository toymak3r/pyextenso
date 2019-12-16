#!/usr/bin/env python
# -*- coding: latin-1 -*-

import json

class Interpretador:

    limite_inferior = -99999
    limite_superior = 99999
    numero = 0
    type = "json"                 # Default format

    def __init__(self, type):
        if type is not None:
            self.type = type

    def setar_limites(self, minimo, maximo):
        try:
            self.limite_inferior = int(minimo)
            self.limite_superior = int(maximo)
        except:
            error = { "error": "Parâmetro informado em formato incorreto.\
                                Deve ser inteiro."}
            return self.formata_saida(error)
            
    def formata_saida(self, resultado):
        if self.type == "json":
            return json.dumps(resultado)

    def extenso(self, numeral):
        if numeral is None:
            return self.formata_saida("número não informado, parâmetro obrigatório")  
        try:
            self.numero = int(numeral)
        except:
            return self.formata_saida("Parâmetro informado em formato incorreto. \
                                       Deve ser inteiro entre {} e {}".format(self.limite_inferior, 
                                                                              self.limite_superior))


        