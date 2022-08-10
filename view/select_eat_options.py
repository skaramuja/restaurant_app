import tkinter as tk
import tkinter.font as font

from view.display import Display


class SelectEatOptions(tk.Frame):
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
        self.label = tk.Label(self, text="Feeling Spontaneous or Particular?", font=(my_font, Display.main_label_size), bg=Display.background_color)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        surprise_me_button = tk.Button(self, text="Surprise Me", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.surprise_me_button_press())
        surprise_me_button.grid(row=1, column=0, padx=8, pady=8)

        picky_button = tk.Button(self, text="I'm Picky", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.picky_button_press())
        picky_button.grid(row=2, column=0, padx=8, pady=8)

        back_button = tk.Button(self, text="Return", width=25, font=my_font, bg=Display.button_background_color, fg=Display.button_text_color, command=lambda: self.return_to_landing_page())
        back_button.grid(row=3, column=0, padx=8, pady=8)

        # Displaying the frame on the container
        self.pack()

    # Return to landing page method
    def return_to_landing_page(self):
        self.main_controller.return_to_landing_page()

    # Handle Surprise Me button selection
    def surprise_me_button_press(self):
        self.main_controller.handle_surprise_me_frame()

    # Handle I'm Picky button selection
    def picky_button_press(self):
        self.main_controller.handle_picky_frame()
