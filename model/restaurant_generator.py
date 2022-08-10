import random

from model.address import Address
from model.data import database_file_name, create_connection
from model.restaurant import Restaurant


class RestaurantGenerator:
    def __init__(self):
        # create a database connection
        self.conn = create_connection(database_file_name)

    def generate_restaurant(self):
        # List of restaurants from joined tables from database
        tuple_of_all_restaurants = join_restaurants_and_addresses_table(self.conn)
        restaurants = []
        for row in tuple_of_all_restaurants:
            address = Address(row[1], row[3], row[4], row[5], row[6])  # Constructing an instance of an Address model
            restaurant = Restaurant(row[0], row[2], address, row[7])  # Constructing an instance of a Restaurant model
            restaurants.append(restaurant)
        if len(restaurants) == 0:
            raise ValueError('No Results Found')
        return random.choice(restaurants)

    # Generates a random restaurants using a for loop to compare elements in a list based on user filters
    def generate_restaurant_with_filters(self, restaurant_list_selection):
        if not restaurant_list_selection:
            return self.generate_restaurant()
        options = filter_restaurants_table_by_user_choice(self.conn, restaurant_list_selection[0])
        for selection in restaurant_list_selection:
            new_list = filter_restaurants_table_by_user_choice(self.conn, selection)
            options = set(options).intersection(new_list)  # Compare sets to find elements that appear in all filters (search results)
        if len(options) == 0:
            raise ValueError('No Results Found')
        random_sample = random.sample(options, 1)
        selection = random_sample[0]
        address = Address(selection[1], selection[3], selection[4], selection[5], selection[6])  # Constructing an instance of an Address model
        restaurant = Restaurant(selection[0], selection[2], address, selection[7])  # Constructing an instance of a Restaurant model
        return restaurant


def join_restaurants_and_addresses_table(conn):
    """Join restaurants and address table to create new table
    :param conn: the connection object
    :return: list of tuples that containing restaurants and addresses columns
    """
    cur = conn.cursor()
    cur.execute("SELECT r.restaurant_id, a.address_id, r.name, a.street, a.city, a.state, a.zip_code, r.rating "
                "FROM restaurants r JOIN addresses a USING(address_id);")
    conn.commit()
    rows = cur.fetchall()

    return rows  # return the rows


def filter_restaurants_table_by_user_choice(conn, choice):
    """filter restaurants by user category choice(s)
    :param conn: the connection object
    :param choice: user selected category choice
    :return: list of tuples that match user's selected category choice
    """
    cur = conn.cursor()

    cur.execute("SELECT r.restaurant_id, a.address_id, r.name, a.street, a.city, a.state, a.zip_code, r.rating "
                "FROM restaurants r JOIN addresses a USING(address_id)"
                "WHERE restaurant_id IN (SELECT restaurant_id"
                "                        FROM restaurant_categories"
                "                        WHERE category_ID IN (SELECT category_ID"
                "                                               FROM categories"
                f"                                               WHERE name = '{choice}'));")

    conn.commit()
    rows = cur.fetchall()

    return rows  # return the rows


def query_restaurants_table_by_name(conn, name):
    """filter restaurants by name
    :param conn: the connection object
    :param name: user selected restaurant name
    :return: list of tuples that match user's selected restaurant name
    """
    cur = conn.cursor()

    cur.execute("SELECT r.restaurant_id, a.address_id, r.name, a.street, a.city, a.state, a.zip_code, r.rating "
                "FROM restaurants r JOIN addresses a USING(address_id)"
                f"WHERE r.name like '{name}%'"
                f"OR r.name like '%{name}%'"
                f"OR r.name like '%{name}';")

    conn.commit()
    rows = cur.fetchall()

    return rows  # return the rows
