class Category:  # Constructor for Restaurant Category Data
    def __init__(self, category_id, name):
        self.__category_id = category_id
        self.__name = name

    def get_category_id(self):
        return self.__category_id

    def get_name(self):
        return self.__name

    def __str__(self):  # Method to format Category properties
        return f'ID: {self.__category_id}, Name: {self.__name},'

    def __repr__(self):  # Method to format Category data type and values
        return f'{type(self.__category_id)} - {self.__category_id}, {type(self.__name)} - {self.__name}'
