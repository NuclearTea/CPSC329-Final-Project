import tkinter as tk
from src.gui.crypto_tool_list import crypto_tool_list
from src.gui.styles import PROGRAM_FONT
from src.gui.characters_tool import component_2
from src.gui.encryption_decryption_tool import component_3
from src.gui.caesar_cipher_tool import component_4


def create_main_window():
    root = tk.Tk()
    root.title("Crypto Tools")
    root.geometry("1600x900")

    # Right content frame that will be updated
    content_frame = tk.Frame(root, bg="white")
    content_frame.pack(side="right", fill="both", expand=True)

    # === Define your 4 components as functions ===
    # These can be defined in another file and then called in each of these function
    def component_1(parent):
        label = tk.Label(
            parent,
            text="This is OTP hex <-> binary",
            font=(PROGRAM_FONT, 18),
            bg="white",
        )
        label.pack(expand=True)

    components = (component_1, component_2, component_3, component_4)

    def on_item_click(index):
        for widget in content_frame.winfo_children():
            widget.destroy()
        components[index](content_frame)

    crypto_tool_list(root, on_item_click)

    # Show the first component by default
    on_item_click(0)

    root.mainloop()
