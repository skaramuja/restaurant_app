import tkinter as tk
import tkinter.font as font

from model.restaurant_generator import RestaurantGenerator
from view.display import Display, display_error


class Picky(tk.Frame):
    def __init__(self, restaurant_controller):
        super().__init__(restaurant_controller)
        self.restaurant_controller = restaurant_controller
        self.choices = []
        self.random_filter_selection = []
        self.generate_restaurant_text_frame = tk.Frame(self)

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
        self.restaurant_controller.select_eat_options_frame()

    def create_widget(self):
        # set font type
        my_font = font.Font(family=Display.my_font)

        # Header Label
        label = tk.Label(self, text="What are you hungry for?", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create an instance of the checkbox frame
        checkbox_frame = CheckBoxFrame(self)
        checkbox_frame.grid(row=1, column=0)

        # Create an instance of the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(row=2, column=0)

    # Adds and removes choice(s) to a list depending on user check box selection
    def handle_choice(self, checkbutton_selection, choice):
        if checkbutton_selection == 0:
            try:
                self.choices.remove(choice)
            except ValueError:
                pass
        else:
            self.choices.append(choice)

    # Passes a list of user choices to generate_restaurant_with_filters method
    def submit_button(self):
        try:
            self.random_filter_selection = RestaurantGenerator().generate_restaurant_with_filters(self.choices)
            self.generate_restaurant_text_frame.destroy()
            # Create an instance of the display restaurant frame when submit button is pressed
            self.generate_restaurant_text_frame = GenerateRestaurantText(self)
            self.generate_restaurant_text_frame.grid(row=3, column=0)
        except ValueError as e:
            display_error(e)


class CheckBoxFrame(tk.Frame):
    def __init__(self, picky_frame):
        super().__init__(picky_frame)

        # Reference of a picky frame
        self.picky_frame = picky_frame

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
        breakfast_checkbutton = tk.Checkbutton(self, text="Breakfast", font=my_font, bg=Display.background_color, variable=breakfast_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(breakfast_value.get(), 'breakfast'))
        breakfast_checkbutton.grid(row=1, column=1, padx=2, pady=2, sticky='w')

        lunch_value = tk.IntVar()
        lunch_checkbutton = tk.Checkbutton(self, text="Lunch", font=my_font, bg=Display.background_color, variable=lunch_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(lunch_value.get(), 'lunch'))
        lunch_checkbutton.grid(row=1, column=2, padx=2, pady=2, sticky='w')

        dinner_value = tk.IntVar()
        dinner_checkbutton = tk.Checkbutton(self, text="Dinner", font=my_font, bg=Display.background_color, variable=dinner_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(dinner_value.get(), 'dinner'))
        dinner_checkbutton.grid(row=1, column=3, padx=2, pady=2, sticky='w')

        # Cuisine label
        food_type_label = tk.Label(self, text="Cuisine:", font=bold_my_font, bg=Display.background_color)
        food_type_label.grid(row=2, column=0, padx=2, pady=2, sticky='e')

        # Cuisine check buttons
        american_value = tk.IntVar()
        american_checkbutton = tk.Checkbutton(self, text="American", font=my_font, bg=Display.background_color, variable=american_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(american_value.get(), 'american'))
        american_checkbutton.grid(row=2, column=1, padx=2, pady=2, sticky='w')

        mexican_value = tk.IntVar()
        mexican_checkbutton = tk.Checkbutton(self, text="Mexican", font=my_font, bg=Display.background_color, variable=mexican_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(mexican_value.get(), 'mexican'))
        mexican_checkbutton.grid(row=2, column=2, padx=2, pady=2, sticky='w')

        italian_value = tk.IntVar()
        italian_checkbutton = tk.Checkbutton(self, text="Italian", font=my_font, bg=Display.background_color, variable=italian_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(italian_value.get(), 'italian'))
        italian_checkbutton.grid(row=2, column=3, padx=2, pady=2, sticky='w')

        bosnian_value = tk.IntVar()
        bosnian_checkbutton = tk.Checkbutton(self, text="Bosnian", font=my_font, bg=Display.background_color, variable=bosnian_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(bosnian_value.get(), 'bosnian'))
        bosnian_checkbutton.grid(row=2, column=4, padx=2, pady=2, sticky='w')

        # Service type label
        service_type_label = tk.Label(self, text="Type:", font=bold_my_font, bg=Display.background_color)
        service_type_label.grid(row=3, column=0, padx=2, pady=2, sticky='e')

        # Service type check buttons
        fast_food_value = tk.IntVar()
        fast_food_checkbutton = tk.Checkbutton(self, text="Fast Food:", font=my_font, bg=Display.background_color, variable=fast_food_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(fast_food_value.get(), 'fast_food'))
        fast_food_checkbutton.grid(row=3, column=1, padx=2, pady=2, sticky='w')

        sit_down_value = tk.IntVar()
        sit_down_checkbutton = tk.Checkbutton(self, text="Sit-down:", font=my_font, bg=Display.background_color, variable=sit_down_value, onvalue=1, offvalue=0, command=lambda: self.picky_frame.handle_choice(sit_down_value.get(), 'sit_down'))
        sit_down_checkbutton.grid(row=3, column=2, padx=2, pady=2, sticky='w')


class ButtonFrame(tk.Frame):
    def __init__(self, picky_frame):
        super().__init__(picky_frame)

        # Reference of a picky frame
        self.picky_frame = picky_frame

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
        self.picky_frame.back_button()

    # Submit food selects method
    def handle_submit_button_press(self):
        self.picky_frame.submit_button()


class GenerateRestaurantText(tk.Frame):
    def __init__(self, picky_frame):
        super().__init__(picky_frame)

        # Reference of a surprise me frame
        self.picky_frame = picky_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Header label
        label = tk.Label(self, text="You should eat at...", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=2, pady=20)

        # Display restaurant label
        generate_restaurant_label = tk.Label(self, text=f'{self.picky_frame.random_filter_selection.get_name()}', font=(my_font, Display.name_text_size), bg=Display.background_color, fg=Display.name_font_color)
        generate_restaurant_label.grid(row=1, column=0, padx=0, pady=0)

        generate_restaurant_address_label = tk.Label(self, text=f'{self.picky_frame.random_filter_selection.get_address().get_street()}', font=(my_font, Display.address_text_size), bg=Display.background_color, fg=Display.address_font_color)
        generate_restaurant_address_label.grid(row=2, column=0, padx=0, pady=0)

        generate_restaurant_address_label = tk.Label(self, text=f'{self.picky_frame.random_filter_selection.get_address().get_city()}, {self.picky_frame.random_filter_selection.get_address().get_state()} {self.picky_frame.random_filter_selection.get_address().get_zipcode()}', font=(my_font, Display.address_text_size), bg=Display.background_color, fg=Display.address_font_color)
        generate_restaurant_address_label.grid(row=3, column=0, padx=0, pady=0)
