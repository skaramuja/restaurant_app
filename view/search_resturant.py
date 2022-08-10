import tkinter as tk
from tkinter import *

from view.display import Display


class SearchRestaurant(tk.Frame):
    def __init__(self, search_restaurant_controller, search_result=None, search_text=""):
        super().__init__(search_restaurant_controller)
        if search_result is None:
            search_result = []
        self.search_restaurant_controller = search_restaurant_controller
        self.search_result = search_result
        self.search_text = search_text

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widget()

        # Displaying the frame on the container
        self.pack()

        # Method to call on edit restaurant controller to return to previous frame
    def back_button(self):
        self.search_restaurant_controller.return_to_landing_page()

    def search_button(self, restaurant_name):
        self.search_restaurant_controller.search_restaurants(restaurant_name)

    def edit_button(self, restaurant):
        self.search_restaurant_controller.edit_restaurant(restaurant)

    def create_widget(self):

        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Header Label
        label = tk.Label(self, text="Search Restaurants", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create an instance of the Search Frame
        search_frame = SearchFrame(self, self.search_result, self.search_text)
        search_frame.grid(row=1, column=0)

        # Create an instance of the Action Button frame
        action_button_frame = ActionButtonFrame(self)
        action_button_frame.grid(row=2, column=0)


class SearchFrame(tk.Frame):
    def __init__(self, search_restaurant_frame, search_result, search_text):
        super().__init__(search_restaurant_frame)
        self.current_searched_text = search_text
        self.search_result = search_result

        # Reference of an update frame
        self.search_restaurant_frame = search_restaurant_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)
        bold_my_font = font.Font(family=Display.my_font, weight="bold")

        # Entry box label
        search_box_label = Label(self, text="Search Restaurant: ", font=bold_my_font, bg=Display.background_color)
        search_box_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        # Entry box to search restaurant
        search_box = tk.Entry(self, width=65)
        search_box.insert(0, self.current_searched_text)
        search_box.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Search button
        search_button = tk.Button(self, text="Search", width=15, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_search_button_press(search_box.get()))
        search_button.grid(row=0, column=2, padx=8, pady=8)

        # Search result label
        for index in range(len(self.search_result)):
            result = self.search_result[index]
            search_result_name_label = tk.Label(self, text=f'{result.get_name()}:', font=(my_font, Display.name_text_size), bg=Display.background_color, fg=Display.name_font_color)
            search_result_name_label.grid(row=index + 1, column=0, padx=5, pady=5, sticky='e')

            search_result_address_label = tk.Label(self, text=f'{str(result.get_address())}', font=(my_font, Display.name_text_size), bg=Display.background_color, fg=Display.name_font_color)
            search_result_address_label.grid(row=index + 1, column=1, padx=5, pady=5, sticky='w')

            # Search button
            edit_button = tk.Button(self, text="Edit", width=15, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda restaurant=result: self.handle_edit_button_press(restaurant))
            edit_button.grid(row=index + 1, column=2, padx=8, pady=8)

    # Handle search button press method
    def handle_search_button_press(self, name):
        self.search_restaurant_frame.search_button(name)

    # Handle edit button press method
    def handle_edit_button_press(self, restaurant):
        self.search_restaurant_frame.edit_button(restaurant)


class ActionButtonFrame(tk.Frame):
    def __init__(self, search_restaurant_frame):
        super().__init__(search_restaurant_frame)

        # Reference of an update frame
        self.search_restaurant_frame = search_restaurant_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Return button
        back_button = tk.Button(self, text="Return", width=20, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.return_to_landing_page())
        back_button.grid(row=0, column=1, padx=8, pady=8)

    # Return to landing page method
    def return_to_landing_page(self):
        self.search_restaurant_frame.back_button()
