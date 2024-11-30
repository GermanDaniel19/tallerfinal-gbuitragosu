from flask import Flask, jsonify, render_template
from models.huron import Huron
from models.boa_Constrictor import Boa_Constrictor
from models.perro import Perro
from models.gato import Gato

app = Flask(__name__,template_folder="views")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/perro")
def perro():
    perro = Perro(5.5,"Budapest","firulai")
    return jsonify({"sonido":perro.hacer_ruido()}),201

@app.route("/gato")
def gato():
    gato = Gato(15.4,"Bogota","gatubelo")
    return jsonify({"sonido":gato.hacer_ruido()}),201

@app.route("/boa")
def boa():
    boa = Boa_Constrictor(15.4,"Amazonas",20.4,"boanacleta")
    return jsonify({"sonido":boa.hacer_ruido()}),201

@app.route("/huron")
def huron():
    huron1 = Huron(5.2,"guinea ecuatorial",115.8)
    return jsonify({"sonido":huron1.hacer_ruido()}),201

if __name__ == '__main__':
    app.run(debug=True)