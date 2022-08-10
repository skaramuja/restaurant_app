import os

import tkinter as tk


class Display:
    # define color patterns
    background_color = '#b3cde0'
    button_background_color = '#03396c'
    button_text_color = 'white'

    # define font
    my_font = 'Helvetica'

    # define label size
    main_label_size = 17

    # define restaurant name text
    name_text_size = 15
    name_font_color = '#f76b8a'

    # define address name text
    address_text_size = 12
    address_font_color = '#f76b8a'

    # define message
    message_size = 15
    error_message_font_color = '#FF4E50'
    success_message_font_color = '#013220'


def display_error(error_message):
    error_root = tk.Tk()
    error_root.title("Error")
    error_root.geometry("300x100")

    # update default icon to error.ico
    folder = os.path.dirname(os.path.abspath(__file__))
    ico_file = os.path.join(folder, 'error.ico')
    error_root.iconbitmap(ico_file)

    error_root.configure(background=Display.background_color)
    label = tk.Label(error_root, font=(Display.my_font, Display.message_size), wraplength=250, justify="center", bg=Display.background_color, fg=Display.error_message_font_color, text=f'{error_message}')
    label.pack()


def display_success(success_message):
    success_root = tk.Tk()
    success_root.title("Restaurant Successfully Updated")
    success_root.geometry("300x100")

    # update default icon to success.ico
    folder = os.path.dirname(os.path.abspath(__file__))
    ico_file = os.path.join(folder, 'success.ico')
    success_root.iconbitmap(ico_file)

    success_root.configure(background=Display.background_color)
    label = tk.Label(success_root, font=(Display.my_font, Display.message_size), wraplength=250, justify="center", bg=Display.background_color, fg=Display.success_message_font_color, text=f'{success_message}')
    label.pack()
