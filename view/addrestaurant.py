import tkinter as tk
import tkinter.font as font

from view.display import Display


class AddRestaurant(tk.Frame):
    def __init__(self, add_controller):
        super().__init__(add_controller)
        self.add_controller = add_controller
        self.name_address_entry = RestaurantNameAddress(self)
        self.rating = Rate(self)
        self.choices = []

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
        self.add_controller.return_to_landing_page()

    def create_widget(self):
        # set font type
        my_font = font.Font(family=Display.my_font)

        # Header Label
        label = tk.Label(self, text="Add Restaurant", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=10, pady=10)

        self.name_address_entry.grid(row=1, column=0)

        # Create an instance of the checkbox frame
        checkbox_frame = CheckBoxFrame(self)
        checkbox_frame.grid(row=2, column=0)

        self.rating.grid(row=3, column=0)

        # Create an instance of the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(row=4, column=0)

    def handle_choice(self, checkbutton_selection, choice):
        if checkbutton_selection == 0:
            try:
                self.choices.remove(choice)
            except ValueError:
                pass
        else:
            self.choices.append(choice)

    def submit_button(self):
        name_address_list = self.name_address_entry.get_input()
        rating_list = self.rating.get_rating_input()
        filter_choice_list = self.choices
        self.add_controller.handle_submission(name_address_list, rating_list, filter_choice_list)


class RestaurantNameAddress(tk.Frame):
    def __init__(self, add_frame):
        super().__init__(add_frame)

        # Reference of an update me frame
        self.add_frame = add_frame

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
        self.restaurant_name_entry.grid(row=0, column=1, sticky='w')

        # Street label
        self.street_label = tk.Label(self, text="Street:", font=bold_my_font, bg=Display.background_color)
        self.street_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        # Street entry
        self.street_entry = tk.Entry(self, width=57)
        self.street_entry.grid(row=1, column=1, sticky='w')

        # City label
        self.city_label = tk.Label(self, text="City:", font=bold_my_font, bg=Display.background_color)
        self.city_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        # City entry
        self.city_entry = tk.Entry(self, width=57)
        self.city_entry.grid(row=2, column=1, sticky='w')

        # State label
        self.state_label = tk.Label(self, text="State:", font=bold_my_font, bg=Display.background_color)
        self.state_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')

        # State entry
        self.state_entry = tk.Entry(self, width=57)
        self.state_entry.grid(row=3, column=1, sticky='w')

        # zip code label
        self.zip_code_label = tk.Label(self, text="Zip Code:", font=bold_my_font, bg=Display.background_color)
        self.zip_code_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')

        # zip code entry
        self.zip_code_entry = tk.Entry(self, width=57)
        self.zip_code_entry.grid(row=4, column=1, sticky='w')

    def get_input(self):
        return [
            self.restaurant_name_entry.get(),
            self.street_entry.get(),
            self.city_entry.get(),
            self.state_entry.get(),
            self.zip_code_entry.get()
        ]


class CheckBoxFrame(tk.Frame):
    def __init__(self, add_frame):
        super().__init__(add_frame)

        # Reference of an update frame
        self.add_frame = add_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    # Add labels and check boxes to the frame
    def create_widgets(self):
        # Set font type
        bold_my_font = font.Font(family=Display.my_font, weight="bold")
        my_font = font.Font(family=Display.my_font)

        # Meal type label
        meal_type_label = tk.Label(self, text="Meal Type:", font=bold_my_font, bg=Display.background_color)
        meal_type_label.grid(row=1, column=0, padx=2, pady=2, sticky='e')

        # Cuisine check buttons
        breakfast_value = tk.IntVar()
        breakfast_checkbutton = tk.Checkbutton(self, text="Breakfast", font=my_font, bg=Display.background_color, variable=breakfast_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(breakfast_value.get(), 'breakfast'))
        breakfast_checkbutton.grid(row=1, column=1, padx=2, pady=2, sticky='w')

        lunch_value = tk.IntVar()
        lunch_checkbutton = tk.Checkbutton(self, text="Lunch", font=my_font, bg=Display.background_color, variable=lunch_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(lunch_value.get(), 'lunch'))
        lunch_checkbutton.grid(row=1, column=2, padx=2, pady=2, sticky='w')

        dinner_value = tk.IntVar()
        dinner_checkbutton = tk.Checkbutton(self, text="Dinner", font=my_font, bg=Display.background_color, variable=dinner_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(dinner_value.get(), 'dinner'))
        dinner_checkbutton.grid(row=1, column=3, padx=2, pady=2, sticky='w')

        # Cuisine label
        food_type_label = tk.Label(self, text="Cuisine:", font=bold_my_font, bg=Display.background_color)
        food_type_label.grid(row=2, column=0, padx=2, pady=2, sticky='e')

        # Cuisine check buttons
        american_value = tk.IntVar()
        american_checkbutton = tk.Checkbutton(self, text="American", font=my_font, bg=Display.background_color, variable=american_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(american_value.get(), 'american'))
        american_checkbutton.grid(row=2, column=1, padx=2, pady=2, sticky='w')

        mexican_value = tk.IntVar()
        mexican_checkbutton = tk.Checkbutton(self, text="Mexican", font=my_font, bg=Display.background_color, variable=mexican_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(mexican_value.get(), 'mexican'))
        mexican_checkbutton.grid(row=2, column=2, padx=2, pady=2, sticky='w')

        italian_value = tk.IntVar()
        italian_checkbutton = tk.Checkbutton(self, text="Italian", font=my_font, bg=Display.background_color, variable=italian_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(italian_value.get(), 'italian'))
        italian_checkbutton.grid(row=2, column=3, padx=2, pady=2, sticky='w')

        bosnian_value = tk.IntVar()
        bosnian_checkbutton = tk.Checkbutton(self, text="Bosnian", font=my_font, bg=Display.background_color, variable=bosnian_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(bosnian_value.get(), 'bosnian'))
        bosnian_checkbutton.grid(row=2, column=4, padx=2, pady=2, sticky='w')

        # Service type label
        service_type_label = tk.Label(self, text="Type:", font=bold_my_font, bg=Display.background_color)
        service_type_label.grid(row=3, column=0, padx=2, pady=2, sticky='e')

        # Service type check buttons
        fast_food_value = tk.IntVar()
        fast_food_checkbutton = tk.Checkbutton(self, text="Fast Food:", font=my_font, bg=Display.background_color, variable=fast_food_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(fast_food_value.get(), 'fast_food'))
        fast_food_checkbutton.grid(row=3, column=1, padx=2, pady=2, sticky='w')

        sit_down_value = tk.IntVar()
        sit_down_checkbutton = tk.Checkbutton(self, text="Sit-down:", font=my_font, bg=Display.background_color, variable=sit_down_value, onvalue=1, offvalue=0, command=lambda: self.add_frame.handle_choice(sit_down_value.get(), 'sit_down'))
        sit_down_checkbutton.grid(row=3, column=2, padx=2, pady=2, sticky='w')


class Rate(tk.Frame):
    def __init__(self, add_frame):
        super().__init__(add_frame)

        # Reference of a surprise me frame
        self.add_frame = add_frame

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
        self.rate_entry.grid(row=0, column=1, sticky='w')

    def get_rating_input(self):
        return [self.rate_entry.get()]


class ButtonFrame(tk.Frame):
    def __init__(self, add_frame):
        super().__init__(add_frame)

        # Reference of an update frame
        self.add_frame = add_frame

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
        self.add_frame.back_button()

    # Submit food selects method
    def handle_submit_button_press(self):
        self.add_frame.submit_button()


class AddRestaurantText(tk.Frame):
    def __init__(self, add_frame):
        super().__init__(add_frame)

        # Reference of a surprise me frame
        self.add_frame = add_frame

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
