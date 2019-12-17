# PyExtenso

Webservice python de tradução de numeral para extenso.

Tecnologias: Python3, Flask

## Heroku
Atual Endereço de testes:
    https://pyextenso.herokuapp.com/
    
## Requeriments
    pip --install -r requirements.txt 

## API

### Tradução Base

    https://pyextenso.herokuapp.com/{numero_a_ser_traduzido}

### Dicionário

Os arquivos de linguagens podem ser enviados em formato json para a raiz da aplicação com as devidas traduções como seguem no exemplo do arquivo "ptbr.json"

    https://pyextenso.herokuapp.com/dict/{nome_da_linguagem}


## Línguas Suportadas

| Linguagem |  Código   | Arquivo   |
| --------- | :-------: | -------   |
| Português |  ptbr     | ptbr.json |

