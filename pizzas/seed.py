from app import Pizza, Restaurant, app, db, RestaurantPizza


def create_seed_data():
  with app.app_context():  
      Pizza.query.delete()
      Restaurant.query.delete()
      db.create_all()
      margarita = Pizza(name="Margarita", ingredients="Dough, Tomato Sauce, Cheese")
      pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    
      pizza_palace = Restaurant(name="Pizza Palace", address="123 Main St")
      dominion_pizza = Restaurant(name="Dominion Pizza", address="456 Elm St")

    
      db.session.add_all([margarita, pepperoni, pizza_palace, dominion_pizza])

    
      db.session.commit()
      print("Added to the database")
      
if __name__ == "__main__":
    create_seed_data()
    
   
    


   