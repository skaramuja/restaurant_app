from model.address import Address
from model.data import database_file_name, create_connection
from model.restaurant import Restaurant
from model.restaurant_generator import query_restaurants_table_by_name


class RestaurantSearcher:
    def __init__(self, name):
        self.name = name

        # Validate Name field
        if len(name) == 0:
            raise ValueError('Restaurant Name cannot be blank')

        # Create a database connection
        self.conn = create_connection(database_file_name)

    # Call on method to query restaurants table and return list of restaurants
    def search_restaurant(self):
        restaurants = []
        query_matches = query_restaurants_table_by_name(self.conn, self.name)
        if not query_matches:
            raise ValueError(f'No matches found for {self.name}')
        for row in query_matches:
            address = Address(row[1], row[3], row[4], row[5], row[6])  # Constructing an instance of an Address model
            restaurant = Restaurant(row[0], row[2], address, row[7])  # Constructing an instance of a Restaurant model
            restaurants.append(restaurant)
        return restaurants
