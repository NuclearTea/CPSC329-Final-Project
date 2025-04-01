import tkinter as tk
from logic.example_logic import example_function


def create_main_window():
    window = tk.Tk()
    window.title("Tkinter App")
    window.geometry("400x300")

    # add random label
    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack(pady=20)

    # add label using function
    label = tk.Label(window, text=example_function())
    label.pack(pady=20)
    return window
