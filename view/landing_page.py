import tkinter as tk
import tkinter.font as font

from view.display import Display


class LandingPage(tk.Frame):
    def __init__(self, main_controller):
        super().__init__(main_controller)
        self.main_controller = main_controller

        # Set up the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        #  Set background color of frame
        self.configure(background=Display.background_color)

        # set font type
        my_font = font.Font(family=Display.my_font)

        # Label
        label = tk.Label(self, text="What do you want to do?", font=(my_font, Display.main_label_size), bg=Display.background_color)
        label.grid(row=0, column=0, padx=20, pady=20)

        # buttons
        eat_button = tk.Button(self, text="Eat", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_eat_button_press())
        eat_button.grid(row=1, column=0, padx=8, pady=8)

        add_edit_restaurant_button = tk.Button(self, text="Add", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_add_button_press())
        add_edit_restaurant_button.grid(row=2, column=0, padx=8, pady=8)

        search_restaurant_button = tk.Button(self, text="Search", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.handle_search_button_press())
        search_restaurant_button.grid(row=3, column=0, padx=8, pady=8)

        cancel_button = tk.Button(self, text="Cancel", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=main_controller.destroy)
        cancel_button.grid(row=4, column=0, padx=8, pady=8)

        # Displaying the frame on the container
        self.pack()

    # handle eat button press
    def handle_eat_button_press(self):
        self.main_controller.handle_generate()

    # handle update button press
    def handle_add_button_press(self):
        self.main_controller.handle_add()

    # handle edit button press
    def handle_search_button_press(self):
        self.main_controller.handle_search()
