import tkinter as tk

from model.restaurant_generator import RestaurantGenerator
from view.picky import Picky
from view.surprise_me import SurpriseMe
from view.display import Display
from view.select_eat_options import SelectEatOptions


class RestaurantController(tk.Frame):
    def __init__(self, main_controller):
        super().__init__(main_controller)
        self.main_controller = main_controller
        self.restaurant_generator = RestaurantGenerator()

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        #  Set background color of frame
        self.configure(background=Display.background_color)

        self.current_frame = SelectEatOptions(self)
        self.pack()

    # Display surprise me frame method
    def handle_surprise_me_frame(self):
        random_restaurant_selection = self.restaurant_generator.generate_restaurant()
        self.current_frame.destroy()
        self.current_frame = SurpriseMe(self, random_restaurant_selection)

    # Display picky frame method
    def handle_picky_frame(self):
        self.current_frame.destroy()
        self.current_frame = Picky(self)

    # Display select eat options frame method
    def select_eat_options_frame(self):
        self.current_frame.destroy()
        self.current_frame = SelectEatOptions(self)

    # return to landing page method
    def return_to_landing_page(self):
        self.current_frame.destroy()
        self.main_controller.return_to_landing_page()
