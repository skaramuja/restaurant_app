from sqlite3 import Error

from model.data import create_connection


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    sql_create_restaurants_table = """ CREATE TABLE IF NOT EXISTS restaurants (
                                        restaurant_id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        address_id integer NOT NULL,
                                        rating integer
                                    ); """

    sql_create_addresses_table = """CREATE TABLE IF NOT EXISTS addresses (
                                    address_id integer PRIMARY KEY AUTOINCREMENT,
                                    street text NOT NULL,
                                    city text NOT NULL,
                                    state text NOT NULL,
                                    zip_code integer NOT NULL,
                                    FOREIGN KEY (address_id) REFERENCES restaurants (address_id)
                                );"""

    sql_create_categories_table = """CREATE TABLE IF NOT EXISTS categories (
                                    category_id integer PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL
                                );"""

    sql_create_restaurantcategories_table = """CREATE TABLE IF NOT EXISTS restaurant_categories (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    restaurant_id integer NOT NULL,
                                    category_id integer NOT NULL,
                                    FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id)
                                    FOREIGN KEY (category_id) REFERENCES categories (category_id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create restaurants table
        create_table(conn, sql_create_restaurants_table)
        # create addresses table
        create_table(conn, sql_create_addresses_table)
        # create categories table
        create_table(conn, sql_create_categories_table)
        # create restaurant_categories table
        create_table(conn, sql_create_restaurantcategories_table)
    else:
        print("Unable to connect to " + str(database))
