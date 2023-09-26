from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import CheckConstraint

db = SQLAlchemy()




class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = "restaurant_pizzas"
    
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))  
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))  
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())
    
    
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
        
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
class Restaurant(db.Model,SerializerMixin):
    __tablename__ = "restaurants"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  
    address = db.Column(db.String)
     
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')
    
class Pizza(db.Model,SerializerMixin):
    __tablename__ = "pizzas"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String)
    
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')
