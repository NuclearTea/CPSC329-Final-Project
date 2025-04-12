import base64
import tkinter as tk
from tkinter import ttk
from Crypto.Random import get_random_bytes

from src.gui.styles import PROGRAM_FONT
from src.logic.aes import encrypt, decrypt
from src.logic.atbash import atbash_cipher
from src.logic.letter_to_number import (
    letter_to_number_encrypt,
    letter_to_number_decrypt,
)


def component_3(parent):
    key = get_random_bytes(32)

    # Set up scrollable container
    container = tk.Frame(parent)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def add_cipher_section(title_text, on_submit):
        # Title
        title = tk.Label(scrollable_frame, text=title_text, font=(PROGRAM_FONT, 25))
        title.pack(anchor="n", pady=(20, 10))

        # Input label
        input_label = tk.Label(
            scrollable_frame,
            text="Please enter the text you wish to encrypt/decrypt:",
            font=(PROGRAM_FONT, 14),
        )
        input_label.pack(anchor="n", pady=(0, 5))

        # Input field
        input_entry = tk.Entry(
            scrollable_frame, font=(PROGRAM_FONT, 16), width=75, borderwidth=2
        )
        input_entry.pack(pady=(0, 20))

        # Encrypt/decrypt selection
        radio_code = tk.IntVar()
        radio_label = tk.Label(
            scrollable_frame,
            text="Select an option to perform:",
            font=(PROGRAM_FONT, 14),
        )
        radio_label.pack()

        tk.Radiobutton(
            scrollable_frame,
            text="Encrypt",
            font=(PROGRAM_FONT, 16),
            variable=radio_code,
            value=0,
        ).pack()
        tk.Radiobutton(
            scrollable_frame,
            text="Decrypt",
            font=(PROGRAM_FONT, 16),
            variable=radio_code,
            value=1,
        ).pack(pady=(0, 10))

        # Output label
        output_label = tk.Label(
            scrollable_frame,
            text="The output will be displayed below:",
            font=(PROGRAM_FONT, 14),
        )
        output_label.pack(pady=(0, 5))

        # Output box (selectable)
        output = tk.Text(
            scrollable_frame, height=4, font=(PROGRAM_FONT, 16), wrap="word"
        )
        output.insert("1.0", ". . .")
        output.config(state="disabled")
        output.pack(fill="x", padx=10)

        # Button action
        def on_click():
            text = input_entry.get()
            encrypt_mode = radio_code.get()
            result = on_submit(text, encrypt_mode)

            output.config(state="normal")
            output.delete("1.0", tk.END)
            output.insert("1.0", result)
            output.config(state="disabled")

        # Submit button
        translate_button = tk.Button(
            scrollable_frame,
            text="Translate!",
            font=(PROGRAM_FONT, 18),
            command=on_click,
        )
        translate_button.pack(pady=(10, 30))

    # AES Section
    aes_title = f"AES (Your key is {base64.b64encode(key).decode('utf-8')})"
    add_cipher_section(
        aes_title,
        lambda text, mode: encrypt(text, key) if mode == 0 else decrypt(text, key),
    )

    # Atbash Section
    add_cipher_section("Atbash", lambda text, mode: atbash_cipher(text))

    # Letter to Number Section
    add_cipher_section(
        "Letter to Number",
        lambda text, mode: letter_to_number_encrypt(text)
        if mode == 0
        else letter_to_number_decrypt(text),
    )

    return container
