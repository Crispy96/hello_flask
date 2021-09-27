from flask import Flask

app = Flask(__name__)

@app.route('/')      #decorador, tras el va una función la cuál le da una función extra, hace que la función sea reconocible por el servidor web
def el_que_os_de_la_gana():
    return 'Hola, que tal mundo!'.upper()

@app.route('/bye')
def otro():
    return "Adios, mundo cruel!"
