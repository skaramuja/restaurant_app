import tkinter as tk

from model.restaurant_updater import RestaurantUpdater
from view.display import Display, display_success, display_error
from view.addrestaurant import AddRestaurant


class AddController(tk.Frame):
    def __init__(self, main_controller):
        super().__init__(main_controller)
        self.main_controller = main_controller

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        #  Set background color of frame
        self.configure(background=Display.background_color)

        self.current_frame = AddRestaurant(self)
        self.pack()

    # return to landing page method
    def return_to_landing_page(self):
        self.current_frame.destroy()
        self.main_controller.return_to_landing_page()

    # Display new update page after submit
    def create_new_update_page(self):
        self.current_frame.destroy()
        self.current_frame = AddRestaurant(self)

    # Parses user input and passes it into the restaurant updater
    def handle_submission(self, name_address_list, rating_list, filter_choices_list):
        name = name_address_list[0]
        street = name_address_list[1]
        city = name_address_list[2]
        state = name_address_list[3]
        zip_code = name_address_list[4]
        rate = rating_list[0]

        try:
            RestaurantUpdater(name, street, city, state, zip_code, rate, filter_choices_list).crate_new_restaurant()
            display_success(f'{name} has been added successfully.')
        except ValueError as e:
            display_error(f'Error: {e}.')
