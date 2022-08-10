import tkinter as tk
import tkinter.font as font

from view.display import Display


class SurpriseMe(tk.Frame):
    def __init__(self, restaurant_controller, restaurant_selection):
        super().__init__(restaurant_controller)
        self.restaurant_controller = restaurant_controller
        self.restaurant_selection = restaurant_selection

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widget()

        # Displaying the frame on the container
        self.pack()

    def create_widget(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Header label
        label = tk.Label(self, text="You should eat at...", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=2, pady=30)

        # Create an instance of the display restaurant frame
        generate_restaurant_text_frame = GenerateRestaurantText(self)
        generate_restaurant_text_frame.grid(row=1, column=0)

        # Create an instance of the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(row=2, column=0)

    # Return to eat frame method
    def back_button(self):
        self.restaurant_controller.select_eat_options_frame()

    def try_again_button(self):
        self.restaurant_controller.handle_surprise_me_frame()


class GenerateRestaurantText(tk.Frame):
    def __init__(self, surprise_me_frame):
        super().__init__(surprise_me_frame)

        # Reference of a surprise me frame
        self.surprise_me_frame = surprise_me_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # Display restaurant label
        generate_restaurant_label = tk.Label(self, text=f'{self.surprise_me_frame.restaurant_selection.get_name()}', font=(my_font, Display.name_text_size), bg=Display.background_color, fg=Display.name_font_color)
        generate_restaurant_label.grid(row=1, column=0, padx=0, pady=0)

        generate_restaurant_address_label = tk.Label(self, text=f'{self.surprise_me_frame.restaurant_selection.get_address().get_street()}', font=(my_font, Display.address_text_size), bg=Display.background_color, fg=Display.address_font_color)
        generate_restaurant_address_label.grid(row=2, column=0, padx=0, pady=0)

        generate_restaurant_address_label = tk.Label(self, text=f'{self.surprise_me_frame.restaurant_selection.get_address().get_city()}, {self.surprise_me_frame.restaurant_selection.get_address().get_state()} {self.surprise_me_frame.restaurant_selection.get_address().get_zipcode()}', font=(my_font, Display.address_text_size), bg=Display.background_color, fg=Display.address_font_color)
        generate_restaurant_address_label.grid(row=3, column=0, padx=0, pady=0)


class ButtonFrame(tk.Frame):
    def __init__(self, surprise_me_frame):
        super().__init__(surprise_me_frame)

        # Reference of a surprise me frame
        self.surprise_me_frame = surprise_me_frame

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Set background color of frame
        self.configure(background=Display.background_color)

        self.create_widgets()

    def create_widgets(self):
        # Set font type
        my_font = font.Font(family=Display.my_font)

        # buttons
        try_again_button = tk.Button(self, text="Try Again", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_try_again_button_press())
        try_again_button.grid(row=4, column=0, padx=2, pady=40)

        back_button = tk.Button(self, text="Return", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_return_button_press())
        back_button.grid(row=4, column=1, padx=2, pady=40)

    # Return to select eat option frame method
    def handle_return_button_press(self):
        self.surprise_me_frame.back_button()

    # Handle try again button press method
    def handle_try_again_button_press(self):
        self.surprise_me_frame.try_again_button()
