from pizzas.app import db
from pizzas.models import Pizza, Restaurant


def create_seed_data():
    
    margarita = Pizza(name="Margarita", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    
    pizza_palace = Restaurant(name="Pizza Palace", address="123 Main St")
    dominion_pizza = Restaurant(name="Dominion Pizza", address="456 Elm St")

    
    db.session.add_all([margarita, pepperoni, pizza_palace, dominion_pizza])

    
    db.session.commit()

if __name__ == "__main__":
    
    from pizzas.app import app
    app.app_context().push()
    db.create_all()

    create_seed_data()

    print("Seed data created successfully.")