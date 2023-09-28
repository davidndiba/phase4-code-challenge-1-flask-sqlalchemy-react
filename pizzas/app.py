from config import Config
from flask import Flask, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from models import RestaurantPizza, Restaurant, Pizza, db 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app,db)
db.init_app(app)

# Routes
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
    return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})


@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')

    if name is None or address is None:
        return jsonify({'error': 'Name and address are required fields'}), 400

    try:
        restaurant = Restaurant(name=name, address=address)
        db.session.add(restaurant)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Restaurant with the same name already exists'}), 400

    return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address}), 201

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    try:
        db.session.delete(restaurant)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Cannot delete restaurant with associated pizzas'}), 400
    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])


@app.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    name = data.get('name')
    ingredients = data.get('ingredients')

    if name is None or ingredients is None:
        return jsonify({'error': 'Name and ingredients are required fields'}), 400

    try:
        pizza = Pizza(name=name, ingredients=ingredients)
        db.session.add(pizza)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Pizza with the same name already exists'}), 400

    return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}), 201


@app.route('/pizzas/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if pizza is None:
        return jsonify({'error': 'Pizza not found'}), 404
    try:
        db.session.delete(pizza)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Cannot delete pizza with associated data'}), 400
    return '', 204




@app.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    if not restaurant_pizzas:
        return jsonify({'message': 'No restaurant pizzas found'}), 404

    pizza_data = []
    for restaurant_pizza in restaurant_pizzas:
        pizza = Pizza.query.get(restaurant_pizza.pizza_id)
        if pizza:
            pizza_info = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients,
                'price': restaurant_pizza.price,
                'restaurant_id': restaurant_pizza.restaurant_id,
            }
            pizza_data.append(pizza_info)

    return jsonify(pizza_data), 200

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({'errors': ['validation errors']}), 400

    try:
        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'errors': ['validation errors']}), 400

    pizza = Pizza.query.get(pizza_id)
    return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})


@app.route('/restaurant_pizzas/<int:id>', methods=['DELETE'])
def delete_restaurant_pizza(id):
    restaurant_pizza = RestaurantPizza.query.get(id)
    if restaurant_pizza is None:
        return jsonify({'error': 'RestaurantPizza not found'}), 404
    try:
        db.session.delete(restaurant_pizza)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Cannot delete RestaurantPizza with associated data'}), 400
    return '', 204


if __name__ == '__main__':
    
    app.run(debug=True, port=5555)
