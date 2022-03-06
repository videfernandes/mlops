from flask import Flask, request, jsonify
from textblob import TextBlob
import pickle

colunas = ['tamanho', 'ano', 'garagem']
modelo = pickle.load(open('modelo.sav', 'rb'))

app = Flask(__name__)


# Definindo rotas


@app.route('/')
def home():
    return "Minha primeira API"


@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return f'Polaridade: {polaridade}'


@app.route('/cotacao/', methods=['POST'])
def cotaca():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])


app.run(debug=True)
