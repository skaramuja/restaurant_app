import tkinter as tk
import tkinter.font as font

from view.display import Display


class EditRestaurant(tk.Frame):
    def __init__(self, search_controller, restaurant):
        super().__init__(search_controller)
        self.restaurant = restaurant
        self.search_controller = search_controller
        self.name_address_entry = EditRestaurantNameAddress(self, restaurant)
        self.rating = EditRating(self, restaurant)

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widget()

        # Displaying the frame on the container
        self.pack()

    # Method to call on restaurant controller to return to previous frame
    def back_button(self):
        self.search_controller.return_to_landing_page()

    def create_widget(self):
        # set font type
        my_font = font.Font(family=Display.my_font)

        # Header Label
        label = tk.Label(self, text="Edit Restaurant", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=10, pady=10)

        self.name_address_entry.grid(row=1, column=0)

        self.rating.grid(row=3, column=0)

        # Create an instance of the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(row=4, column=0)

    def submit_button(self):
        name_address_list = self.name_address_entry.get_input()
        rating_list = self.rating.get_rating_input()
        self.search_controller.update_restaurant(self.restaurant, name_address_list, rating_list)


class EditRestaurantNameAddress(tk.Frame):
    def __init__(self, edit_frame, restaurant):
        super().__init__(edit_frame)
        self.restaurant = restaurant

        # Reference of an update me frame
        self.edit_frame = edit_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        # Set font type
        bold_my_font = font.Font(family=Display.my_font, weight="bold")

        # Restaurant name label
        self.name_label = tk.Label(self, text="Name:", font=bold_my_font, bg=Display.background_color)
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        # Restaurant name entry
        self.restaurant_name_entry = tk.Entry(self, width=57)
        self.restaurant_name_entry.insert(0, self.restaurant.get_name())
        self.restaurant_name_entry.grid(row=0, column=1, sticky='w')

        # Street label
        self.street_label = tk.Label(self, text="Street:", font=bold_my_font, bg=Display.background_color)
        self.street_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        # Street entry
        self.street_entry = tk.Entry(self, width=57)
        self.street_entry.insert(0, self.restaurant.get_address().get_street())
        self.street_entry.grid(row=1, column=1, sticky='w')

        # City label
        self.city_label = tk.Label(self, text="City:", font=bold_my_font, bg=Display.background_color)
        self.city_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        # City entry
        self.city_entry = tk.Entry(self, width=57)
        self.city_entry.insert(0, self.restaurant.get_address().get_city())
        self.city_entry.grid(row=2, column=1, sticky='w')

        # State label
        self.state_label = tk.Label(self, text="State:", font=bold_my_font, bg=Display.background_color)
        self.state_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')

        # State entry
        self.state_entry = tk.Entry(self, width=57)
        self.state_entry.insert(0, self.restaurant.get_address().get_state())
        self.state_entry.grid(row=3, column=1, sticky='w')

        # zip code label
        self.zip_code_label = tk.Label(self, text="Zip Code:", font=bold_my_font, bg=Display.background_color)
        self.zip_code_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')

        # zip code entry
        self.zip_code_entry = tk.Entry(self, width=57)
        self.zip_code_entry.insert(0, self.restaurant.get_address().get_zipcode())
        self.zip_code_entry.grid(row=4, column=1, sticky='w')

    def get_input(self):
        return [
            self.restaurant_name_entry.get(),
            self.street_entry.get(),
            self.city_entry.get(),
            self.state_entry.get(),
            self.zip_code_entry.get()
        ]


class EditRating(tk.Frame):
    def __init__(self, edit_frame, restaurant):
        super().__init__(edit_frame)
        self.restaurant = restaurant

        # Reference of a surprise me frame
        self.edit_frame = edit_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        # Set font type
        bold_my_font = font.Font(family=Display.my_font, weight="bold")

        # Rating label
        self.rate_label = tk.Label(self, text="Rating:", font=bold_my_font, bg=Display.background_color)
        self.rate_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        # Rating entry
        self.rate_entry = tk.Entry(self, width=57)
        self.rate_entry.insert(0, self.restaurant.get_rating())
        self.rate_entry.grid(row=0, column=1, sticky='w')

    def get_rating_input(self):
        return [self.rate_entry.get()]


class ButtonFrame(tk.Frame):
    def __init__(self, edit_frame):
        super().__init__(edit_frame)

        # Reference of an update frame
        self.edit_frame = edit_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    # Add buttons to the frame
    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Buttons
        submit_button = tk.Button(self, text="Submit", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_submit_button_press())
        submit_button.grid(row=0, column=0, padx=8, pady=8)

        back_button = tk.Button(self, text="Return", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_return_button_press())
        back_button.grid(row=0, column=1, padx=8, pady=8)

    # Return to select eat option method
    def handle_return_button_press(self):
        self.edit_frame.back_button()

    # Submit food selects method
    def handle_submit_button_press(self):
        self.edit_frame.submit_button()


class EditRestaurantText(tk.Frame):
    def __init__(self, edit_frame):
        super().__init__(edit_frame)

        # Reference of a surprise me frame
        self.edit_restaurant = edit_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Text label
        label = tk.Label(self, text="Your changes have been saved successfully", font=(my_font, Display.name_text_size), bg=Display.background_color, fg=Display.address_font_color)
        label.grid(row=0, column=0, padx=2, pady=20)
