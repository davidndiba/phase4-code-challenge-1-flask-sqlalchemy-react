from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from app import db 

# app = create_app()
db = SQLAlchemy()
Base = declarative_base()

class RestaurantPizza(Base):
    __tablename__ = "restaurant_pizzas"
    
    id = Column(Integer, primary_key=True)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'))  
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  
    price = Column(Float, nullable=False)
    
    
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
    
    created_at = Column(Integer)
    updated_at = Column(Integer)
    
    
    pizza = relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = relationship('Restaurant', back_populates='restaurant_pizzas')
class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)  # Adding validation for name
    address = Column(String)
     
    
    restaurant_pizzas = relationship('RestaurantPizza', back_populates='restaurant')
    
class Pizza(Base):
    __tablename__ = "pizzas"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    
    
    restaurant_pizzas = relationship('RestaurantPizza', back_populates='pizza')
