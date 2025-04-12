import tkinter as tk
from src.gui.styles import PROGRAM_FONT

from src.logic.caesar_cipher_logic import caesar_cipher, handle_shift


def component_4(parent):
    frame = tk.Frame(parent)

    title = tk.Label(
        master=frame, 
        text='Caesar Cipher Translator',
        font=('Ariel bold', 25),
        justify='center'
    )
    title.pack(anchor='n', pady=(0, 50))

    input_label = tk.Label(
        master=frame, 
        text='Please enter the text you wish to encrypt/decrypt below:',
        font=('Ariel', 14),
        justify='center'
    )
    input_label.pack(anchor='n', pady=(0, 10))

    input_entry = tk.Entry(
        master=frame,
        font=('Ariel', 16),
        width=75,
        borderwidth=2,
    )
    input_entry.pack(pady=(0, 40))


    shift_label = tk.Label(
        master=frame, 
        text='Please enter number of characters you would like to shift.',
        font=('Ariel', 14),
        justify='center'
    )
    shift_label.pack(pady=(0, 5))

    shift_warning = tk.Label(
        master=frame, 
        text='INTEGERS ONLY. NO SHIFT WILL BE APPLIED OTHERWISE.',
        font=('Ariel', 12),
        justify='center',
        fg='red'
    )
    shift_warning.pack(pady=(0, 10))

    shift_entry = tk.Entry(
        master=frame,
        font=('Ariel', 32),
        width=5,
        borderwidth=2,
    )
    shift_entry.pack(pady=(0, 35))

    radio_code = tk.IntVar()

    radio_label = tk.Label(
        text='Select an option to perform:',
        font=('Ariel', 14)
    )
    radio_label.pack(pady=(0, 5))

    en = tk.Radiobutton(
        master=frame,
        text='Encrypt',
        font=('Ariel', 16),
        variable=radio_code,
        value=0
    )
    en.pack()

    de = tk.Radiobutton(
        master=frame,
        text='Decrypt',
        font=('Ariel', 16),
        variable=radio_code,
        value=1
    )
    de.pack(pady=(0, 50))

    def cmds():
        out = (input_entry.get())
        shft = handle_shift((shift_entry.get()))
        en_de = radio_code.get()
        output.config(text=caesar_cipher(out, shft, en_de))
  
    translate_button = tk.Button(
        master=frame,
        text='Translate!',
        font=('Ariel', 25),
        borderwidth=2,
        command=cmds 
    )
    translate_button.pack(pady=(0, 75))

    output_label = tk.Label(
        master=frame, 
        text='The output will be displayed below:',
        font=('Ariel', 14),
        justify='center',
    )
    output_label.pack(pady=(0, 5))

    output = tk.Label(
        text='. . .',
        master=frame,
        font=('Ariel', 16),
        borderwidth=2,
    )
    output.pack()



    return frame