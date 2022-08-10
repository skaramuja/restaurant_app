class Restaurant:  # Constructor for Restaurant Data
    def __init__(self, restaurant_id, name, address, rating):
        self.__restaurant_id = restaurant_id
        self.__name = name
        self.__address = address
        self.__rating = rating

    def get_restaurant_id(self):
        return self.__restaurant_id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_rating(self):
        return self.__rating

    def __str__(self):  # Method to format restaurant properties
        return f'ID: {self.__restaurant_id}: Restaurant Name: {self.__name}, Address: {self.__address},' \
                f'Rating: {self.__rating}'

    def __repr__(self):  # Method to format restaurant data type and values
        return f'{type(self.__restaurant_id)} - {self.__restaurant_id}, {type(self.__name)} - {self.__name},' \
               f'{type(self.__address)} - {self.__address}, {type(self.__rating)} - {self.__rating}'
