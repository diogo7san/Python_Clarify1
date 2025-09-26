r"""
 ____  _                     ____              _                    
|  _ \(_) ___   __ _  ___   / ___|  __ _ _ __ | |_ __ _ _ __   __ _ 
| | | | |/ _ \ / _` |/ _ \  \___ \ / _` | '_ \| __/ _` | '_ \ / _` |
| |_| | | (_) | (_| | (_) |  ___) | (_| | | | | || (_| | | | | (_| |
|____/|_|\___/ \__, |\___/  |____/ \__,_|_| |_|\__\__,_|_| |_|\__,_|
               |___/                                                

Autor: Diogo Santana
Versão: 0.0.0.1
Data: 25-09-2025
"""
#flask é uma biblioteca diferente. Ele é um miniframework. É um compêndio de várias bibliotecas trabalhando juntas.
#flask -> jango -> ...
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return " <h1>Bem vindo à minha página </h1> <a href='/sobre' Sobre <a> <br> <a> saudacao </a>"

@app.route('/sobre')
def informacoes():
    return "<marquee> Diogo Pereira de Santana </marquee>"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"<h1> Bem vindo </h1>{nome}!"

if __name__ == '__main__':
    app.run(debug=True)

