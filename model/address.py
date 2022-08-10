class Address:  # Constructor for Restaurant Address Data
    def __init__(self, address_id, street, city, state, zip_code):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code

    def get_address_id(self):
        return self.__address_id

    def get_street(self):
        return self.__street

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zipcode(self):
        return self.__zip_code

    def __str__(self):  # Method to format restaurant address properties
        return f'{self.__street}, {self.__city}, {self.__state}, {self.__zip_code}'

    def __repr__(self):  # Method to format restaurant address data type and values
        return f'{type(self.__address_id)} - {self.__address_id}, {type(self.__street)} - {self.__street},' \
               f'{type(self.__city)} - {self.__city}, {type(self.__state)} - {self.__state}, {type(self.__zip_code)} - ' \
               f'{self.__zip_code}'
