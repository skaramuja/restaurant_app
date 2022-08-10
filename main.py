"""
Program: main.py
Author: Sabina Johnson
Last date modified: 07/30/2022

The purpose of this program is to edit, view, add, and randomly display restaurants.
The input is user filter selection and adding a restaurant into GUI.
The output is a randomly generated restaurant based on user input.
"""

import os

from controller.main_controller import MainController
from model.csv_importer import RestaurantImporter, AddressImporter, CategoryImporter, RestaurantCategoriesImporter
from model.data import create_connection, create_restaurant, create_address, create_category, \
    create_restaurant_category, database_file_name
from model.tables import create_tables


def create_tables_and_seed_database():
    if os.path.exists(database_file_name):
        pass
    else:
        create_tables(database_file_name)

        # create a database connection
        conn = create_connection(database_file_name)

        # Seed restaurant table from restaurants.csv file
        restaurants = RestaurantImporter().get_data()
        for restaurant in restaurants:
            create_restaurant(conn, (restaurant[0], restaurant[1], restaurant[2]))

        # Seed addresses table from addresses.csv file
        addresses = AddressImporter().get_data()
        for address in addresses:
            create_address(conn, (address[0], address[1], address[2], address[3]))

        # Seed categories table from category.csv file
        categories = CategoryImporter().get_data()
        for category in categories:
            create_category(conn, (category[0], category[1]))

        # Seed restaurant_categories table from restaurantcategories.csv file
        restaurant_categories = RestaurantCategoriesImporter().get_data()
        for restaurant_category in restaurant_categories:
            create_restaurant_category(conn, (restaurant_category[0], restaurant_category[1]))


if __name__ == '__main__':
    create_tables_and_seed_database()
    app = MainController()  # Create a GUI app
    app.mainloop()  # Make the loop for displaying the app
