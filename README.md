#phase4-code-challenge-1-flask-sqlalchemy-react
 Restaurant Pizza Management System
#
Table of Contents
-Introduction
-Features
-Getting Started
-Prerequisites
-Installation
-Running the Application
-Usage
-Database Schema
-Contributing
-license
-Author

#
Introduction
The Restaurant Pizza Management System is a web application built with Flask that simplifies the management of restaurant information and their pizza offerings. This system provides a user-friendly interface to add, view, and delete restaurants, pizzas, and their associations, making it an ideal tool for restaurant owners and managers.

####
Features
Restaurant Management: Easily add new restaurants, view existing restaurants, and remove unwanted ones. Each restaurant is associated with a name and address and a diiferent id.

Pizza Management: Efficiently manage your pizza menu by adding new pizza types, viewing existing pizzas, and removing items. Each pizza has a name and a list of ingredients and a specific id.

Restaurant-Pizza Associations: Seamlessly create and update associations between restaurants and pizzas, complete with customizable prices. This feature enables you to tailor your menu offerings for each restaurant.

#Getting Started
#Prerequisites
Before you begin, ensure you have met the following requirements:

Python (version >= 3.6)
pip (Python package manager)
Git (optional)
Installation
Clone the repository (if you haven't already) to your local machine:


##Copy code
git clone https://github.com/davidndiba/phase4-code-challenge-1-flask-sqlalchemy-react


Navigate to the project directory:

shell
Copy code
cd restaurant-pizza-management
Install the required dependencies:


shell
Copy code
python app.py
Access the web application by opening a web browser and navigating to http://localhost:5555.

#Usage
###
Restaurant Management:

Click on the "Restaurants" tab to view the list of restaurants.
Click "Add Restaurant" to create a new restaurant.
Click on a restaurant to view its details or delete it.
Pizza Management:

Click on the "Pizzas" tab to view the list of pizza types.
Click "Add Pizza" to create a new pizza type.
Click on a pizza to view its details or delete it.
##
Restaurant-Pizza Associations:

Click on the "Restaurant Pizzas" tab to view existing associations.
Click "Add Association" to create a new association.
Click on an association to view its details or delete it.
##
Database Schema
The application uses the following database schema:

restaurants: Stores restaurant information.
pizzas: Stores pizza information.
restaurant_pizzas: Stores associations between restaurants and pizzas, including prices.
 
 
 ##
 #Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the Contributing Guidelines.

##
Author
David Muthua Ndiba

## License
MIT license Copyright (c) 2023 <David>


Permission is hereby granted,free of charge , for any person obtaining a copy of this software and associated documentation files(the "software"),to deal in the Software without restriction ,including without limitaion the rights to use,copy,modify,merge,publish,distribute,sublicense,and/or sell copies of the Software ,and to permit persons to whom the Software is furnished to do so,subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the software.

THE SOFTWAREBIS PROVIDED "AS IS",WITHOUT WARRANTY OF ANY KIND ,EXPRESS OR IMPLIED ,INCUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY ,FITNESS FOR A PURPOSE AND NONIINFRINGEMENT.IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,DAMAGES OR OTHER LIABILITIES,WHETHER IN AN ACTION OF CONTRACT TORT OR OTHERWISE ,ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR USE OTHER DEALINGS IN THE SOFTWARE.