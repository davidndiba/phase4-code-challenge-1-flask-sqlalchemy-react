from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

db = SQLAlchemy()
Base = declarative_base()


class Restaurant_Pizzas(Base):
    __tablename__ = "restaurant_pizzas"
    
    id = Column(Integer(), primary_key=True)
    pizza_id = Column(Integer(),)
    restaurant_id = Column(Integer(),)
    price = Column(Integer(),)
    created_at = Column(Integer(),)
    updated_at = Column(Integer(),) 
    

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(),)
    address =Column(Integer(),)
     
    # Define relationships here

class Pizza(Base):
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True)
    name = Column(String(), )
    ingredients = Column(String(),)
    created_at = Column(Integer(),)
    updated_at = Column(Integer(),)
    # Define relationships here
