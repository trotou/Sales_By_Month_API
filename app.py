from unicodedata import category
from flask import Flask, request, jsonify
from flask_cors import CORS
from database.db import food, clothes

app = Flask(__name__)

CORS(app)


@app.route('/products')
def list_products():       
    try: 
        result = []
        result = food[0]['comida'] + clothes[0]['roupas'] + food[1]['bebidas'] + clothes[1]['acessórios']
        return jsonify(result)
    except:
        return ('', 400)

@app.route('/products/get_product')
@app.route('/products/get_product/<product>')
def get_product(product=''):       
    try: 
        if product == 'comida':
            return jsonify([{'key': 'All', 'value': 'all'}, {'key': 'comida', 'value': 'comida'}, {'key': 'bebidas', 'value': 'bebidas'}])
        if product == 'roupas':
            return jsonify([{'key': 'All', 'value': 'all'}, {'key': 'roupas', 'value': 'roupas'}, {'key': 'acessorios', 'value': 'acessorios'}])
        return jsonify([])
    except:
        return ('', 400)


@app.route('/products/get_brands')
@app.route('/products/get_brands/<name>')
def get_products(name=''):       
    try: 
        if name == 'bebidas':
            result = list(dict.fromkeys([d['brand'] for d in food[1]['bebidas']])) 
            for i in range(len(result)):
                result[i] = {'key': result[i], 'value': result[i]}
            return jsonify(result)

        if name == 'roupas':
            result = list(dict.fromkeys([d['brand'] for d in clothes[0]['roupas']])) 
            for i in range(len(result)):
                result[i] = {'key': result[i], 'value': result[i]}
            return jsonify(result)

        if name == 'acessorios':
            result = list(dict.fromkeys([d['brand'] for d in clothes[1]['acessórios']])) 
            for i in range(len(result)):
                result[i] = {'key': result[i], 'value': result[i]}
            return jsonify(result)

        if name == 'comida':
            result = list(dict.fromkeys([d['brand'] for d in food[0]['comida']])) 
            for i in range(len(result)):
                result[i] = {'key': result[i], 'value': result[i]}
            return jsonify(result) 

        return jsonify([])
    except:
        return ('', 400)


@app.route('/products/filter_by_brand/<category>/<brand>')
def filter_by_brand(brand='', category=''):
    try: 
        if category == 'comida':
            result = [d for d in food[0]['comida'] if d['brand'] == brand]
            return jsonify(result)

        if category == 'roupas':
            result = [d for d in clothes[0]['roupas'] if d['brand'] == brand]
            return jsonify(result)

        if category == 'acessorios':
            result = [d for d in clothes[1]['acessórios'] if d['brand'] == brand]
            return jsonify(result)

        if category == 'bebidas':
            result = [d for d in food[1]['bebidas'] if d['brand'] == brand]
            return jsonify(result)

        return jsonify([])
    except:
        return ('', 400)



@app.route('/food')
def list_food():
    try:
        return jsonify(food[0]['comida'] + food[1]['bebidas'])
    except:
        return ('', 400)


@app.route('/food/comidas')
def list_food_comida():
    try:
        return jsonify(food[0]['comida'])
    except:
        return ('', 400)


@app.route('/food/bebidas')
def list_food_bebidas():
    try:
        return jsonify(food[1]['bebidas'])
    except:
        return ('', 400)


@app.route('/clothes')
def list_clothes():
    try:
        return jsonify(clothes[1]['acessórios'] + clothes[0]['roupas'])
    except:
        return ('', 400)


@app.route('/clothes/roupas')
def list_clothes_roupas():
    try:
        return jsonify(clothes[0]['roupas'])
    except:
        return ('', 400)


@app.route('/clothes/acessorios')
def list_clothes_acessorios():
    try:
        return jsonify(clothes[1]['acessórios'])
    except:
        return ('', 400)

