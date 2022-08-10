import os
import tkinter as tk

from controller.search_restaurants_controller import SearchRestaurantController
from controller.restaurant_controller import RestaurantController
from controller.add_controller import AddController
from view.display import Display
from view.landing_page import LandingPage


class MainController(tk.Tk):
    def __init__(self):
        super().__init__()

        # Constructing the root window
        self.title("Welcome, Let's Eat!")
        self.geometry('800x800')
        self.configure(background=Display.background_color)

        # update default icon to food.ico
        folder = os.path.dirname(os.path.abspath(__file__))
        ico_file = os.path.join(folder, 'food.ico')
        self.iconbitmap(ico_file)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.current_frame = LandingPage(self)

    # Display select eat option frame method
    def handle_generate(self):
        self.current_frame.destroy()
        self.current_frame = RestaurantController(self)

    # Display landing page method
    def return_to_landing_page(self):
        self.current_frame.destroy()
        self.current_frame = LandingPage(self)

    # Display update restaurants frame method
    def handle_add(self):
        self.current_frame.destroy()
        self.current_frame = AddController(self)

    def handle_search(self):
        self.current_frame.destroy()
        self.current_frame = SearchRestaurantController(self)
