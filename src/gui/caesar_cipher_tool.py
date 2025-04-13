import tkinter as tk
from tkinter import ttk
from src.gui.styles import PROGRAM_FONT

from src.logic.caesar_cipher_logic import caesar_cipher, handle_shift


def component_4(parent):
    container = tk.Frame(parent)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas)

    frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    title = tk.Label(
        master=frame,
        text="Caesar Cipher Translator",
        font=(PROGRAM_FONT, 25),
        justify="center",
    )
    title.pack(anchor="n", pady=(20, 10))

    input_label = tk.Label(
        master=frame,
        text="Please enter the text you wish to encrypt/decrypt below:",
        font=(PROGRAM_FONT, 14),
        justify="center",
    )
    input_label.pack(anchor="n", pady=(0, 5))

    input_entry = tk.Entry(
        master=frame,
        font=(PROGRAM_FONT, 16),
        width=75,
        borderwidth=2,
    )
    input_entry.pack(pady=(0, 20))

    shift_label = tk.Label(
        master=frame,
        text="Please enter number of characters you would like to shift.",
        font=(PROGRAM_FONT, 14),
        justify="center",
    )
    shift_label.pack(pady=(0, 5))

    shift_warning = tk.Label(
        master=frame,
        text="INTEGERS ONLY. NO SHIFT WILL BE APPLIED OTHERWISE.",
        font=(PROGRAM_FONT, 12),
        justify="center",
        fg="red",
    )
    shift_warning.pack(pady=(0, 10))

    shift_entry = tk.Entry(
        master=frame,
        font=(PROGRAM_FONT, 32),
        width=5,
        borderwidth=2,
    )
    shift_entry.pack(pady=(0, 20))

    radio_code = tk.IntVar()

    radio_label = tk.Label(
        master=frame, text="Select an option to perform:", font=(PROGRAM_FONT, 14)
    )
    radio_label.pack(pady=(0, 5))

    tk.Radiobutton(
        master=frame,
        text="Encrypt",
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=0,
    ).pack()

    tk.Radiobutton(
        master=frame,
        text="Decrypt",
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=1,
    ).pack(pady=(0, 20))

    output_label = tk.Label(
        master=frame,
        text="The output will be displayed below:",
        font=(PROGRAM_FONT, 14),
        justify="center",
    )
    output_label.pack(pady=(10, 5))

    output = tk.Text(master=frame, height=4, font=(PROGRAM_FONT, 16), wrap="word")
    output.insert("1.0", ". . .")
    output.config(state="disabled")
    output.pack(fill="x", padx=10)

    def cmds():
        out = input_entry.get()
        shft = handle_shift(shift_entry.get())
        en_de = radio_code.get()
        result = caesar_cipher(out, shft, en_de)

        output.config(state="normal")
        output.delete("1.0", tk.END)
        output.insert("1.0", result)
        output.config(state="disabled")

    translate_button = tk.Button(
        master=frame,
        text="Translate!",
        font=(PROGRAM_FONT, 20),
        borderwidth=2,
        command=cmds,
    )
    translate_button.pack(pady=(10, 30))

    explanation = tk.Label(
        font=(PROGRAM_FONT, 14),
        text="""This tool encodes/decodes text using the Caesar Cipher.
        
        The Caesar Cipher works by shifting every letter in a message down the 
        alphabet a certain number of times.

        This is one of the oldest encryption schemes, said to have been 
        utilized by and named after Julius Caesar!

        This cipher is not secure enough to be seriously implemented today
        however, it holds great merit in introducing basic cryptography in education
        due to its simplicity and effectiveness in demonstrating encryption/decryption.
        """
    )
    explanation.pack()

    return container
