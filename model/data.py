import os
import sqlite3
from sqlite3 import Error

folder = os.path.dirname(os.path.abspath(__file__))
database_file_name = os.path.join(folder, 'restaurants.db')


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_restaurant(conn, restaurant):
    """Create a new restaurant for table
    :param conn:
    :param restaurant:
    :return: id
    """
    print(restaurant)
    sql = ''' INSERT INTO restaurants(name, address_id, rating)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, restaurant)
    conn.commit()

    return cur.lastrowid


def create_address(conn, address):
    """Create a new address for table
    :param conn:
    :param address:
    :return: id
    """
    print(address)
    sql = ''' INSERT INTO addresses(street, city, state, zip_code)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, address)
    conn.commit()

    return cur.lastrowid


def create_category(conn, category):
    """Create a new category for table
    :param conn:
    :param category:
    :return: id
    """
    print(category)
    sql = ''' INSERT INTO categories(category_id, name)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, category)
    conn.commit()

    return cur.lastrowid


def create_restaurant_category(conn, restaurant_category):
    """Create a new restaurant category for table
    :param conn:
    :param restaurant_category:
    :return: id
    """
    sql = ''' INSERT INTO restaurant_categories(restaurant_id, category_id)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, restaurant_category)
    conn.commit()

    return cur.lastrowid


def query_category_table(conn, category):
    """Query category table for a specified category and return the corresponding category_id
    :param conn:
    :param category:
    :return: category_id
    """
    cur = conn.cursor()  # cursor object

    cur.execute(f"SELECT category_id FROM categories WHERE name = '{category}' ")

    conn.commit()
    row = cur.fetchone()

    return row[0]  # returning category_id associated with selected filter choice


def update_address_table(conn, restaurant_id, street, city, state, zip_code):
    """Update address table using user input
    :param conn:
    :param restaurant_id:
    :param street:
    :param city:
    :param state:
    :param zip_code:
    :return:
    """
    cur = conn.cursor()  # cursor object

    cur.execute(f"UPDATE addresses SET street = '{street}', city = '{city}', state = '{state}', zip_code = '{zip_code}' "
                f"WHERE address_id = (SELECT address_id FROM restaurants WHERE restaurant_id = '{restaurant_id}');")

    conn.commit()

    return cur.lastrowid


def update_restaurant_table(conn, restaurant_id, name, rating):
    """QUpdated restaurant table using user input
    :param conn:
    :param restaurant_id:
    :param name:
    :param rating:
    :return:
    """
    cur = conn.cursor()  # cursor object

    cur.execute(f"UPDATE restaurants SET name = '{name}', rating = '{rating}'"
                f"WHERE restaurant_id = '{restaurant_id}';")

    conn.commit()

    return cur.lastrowid
