import tkinter as tk

from model.restaurant_searcher import RestaurantSearcher
from model.restaurant_updater import RestaurantUpdater
from view.display import Display, display_success, display_error
from view.edit_restaurant import EditRestaurant
from view.search_resturant import SearchRestaurant


class SearchRestaurantController(tk.Frame):
    def __init__(self, main_controller):
        super().__init__(main_controller)
        self.main_controller = main_controller

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        #  Set background color of frame
        self.configure(background=Display.background_color)

        self.current_frame = SearchRestaurant(self)
        self.pack()

    # Return to landing page method
    def return_to_landing_page(self):
        self.current_frame.destroy()
        self.main_controller.return_to_landing_page()

    # Call into database to search query and validate input
    def search_restaurants(self, name):
        try:
            search_result = RestaurantSearcher(name).search_restaurant()
            self.current_frame.destroy()
            self.current_frame = SearchRestaurant(self, search_result, name)
        except ValueError as e:
            display_error(f'Error: {e}.')

    def edit_restaurant(self, restaurant):
        self.current_frame.destroy()
        self.current_frame = EditRestaurant(self, restaurant)

    def update_restaurant(self, restaurant, name_address_list, rating_list):
        name = name_address_list[0]
        street = name_address_list[1]
        city = name_address_list[2]
        state = name_address_list[3]
        zip_code = name_address_list[4]
        rate = rating_list[0]

        try:
            RestaurantUpdater(name, street, city, state, zip_code, rate).update_restaurant(restaurant)
            display_success(f'Restaurant has been successfully updated.')
        except ValueError as e:
            display_error(f'Error: {e}.')
