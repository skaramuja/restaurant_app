from model.data import create_address, create_restaurant, query_category_table, create_restaurant_category, \
    update_address_table, update_restaurant_table, database_file_name, create_connection


class RestaurantUpdater:
    def __init__(self, name, street, city, state, zip_code, rating, choice_list=None):

        # Validate Name field
        if choice_list is None:
            choice_list = []
        if len(name) == 0:
            raise ValueError('Name cannot be blank')

        # Validate Street field
        if len(street) == 0:
            raise ValueError('Street cannot be blank')

        # Validate City field
        if len(city) == 0:
            raise ValueError('City cannot be blank')

        # Validate State field
        if len(state) == 0:
            raise ValueError('State cannot be blank')

        # Validate Zip Code field
        if len(zip_code) == 0:
            raise ValueError('Zip Code cannot be blank')

        # Validate that zip code is an integer with number characters, raise ValueError with print message
        number_characters = set("0123456789-")
        if not (number_characters.issuperset(zip_code) and number_characters.issuperset(rating)):
            raise ValueError('Zip Code must be an integer')

        # Validate if rating is an integer and between 1-5, raise ValueError with print message
        try:
            if int(rating) < 1 or int(rating) > 5:
                raise ValueError
        except ValueError:
            raise ValueError('Rating must be an integer between 1-5')

        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = int(zip_code)
        self.rating = int(rating)
        self.choice_list = choice_list

        # create a database connection
        self.conn = create_connection(database_file_name)

    # Add new restaurant to database
    def crate_new_restaurant(self):
        address_id = create_address(self.conn, (self.street, self.city, self.state, self.zip_code))
        restaurant_id = create_restaurant(self.conn, (self.name, address_id, self.rating))
        for choice in self.choice_list:  # loop to obtain category_id for each choice
            category_id = query_category_table(self.conn, choice)
            create_restaurant_category(self.conn, (restaurant_id, category_id))  # pass in tuple containing restaurant_id and category_id

    # Update restaurant and address table based on user input
    def update_restaurant(self, restaurant):
        update_address_table(self.conn, restaurant.get_restaurant_id(), self.street, self.city, self.state, self.zip_code)
        update_restaurant_table(self.conn, restaurant.get_restaurant_id(), self.name, self.rating)
