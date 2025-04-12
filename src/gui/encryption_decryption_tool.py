import base64
import tkinter as tk

from Crypto.Random import get_random_bytes

from src.gui.styles import PROGRAM_FONT

from src.logic.aes import encrypt, decrypt
from src.logic.atbash import atbash_cipher
from src.logic.letter_to_number import letter_to_number_encrypt, letter_to_number_decrypt


def component_3(parent):
    key = get_random_bytes(32)
    frame = tk.Frame(parent)

    title = tk.Label(
        master=frame,
        text='AES (Your key is ' + base64.b64encode(key).decode('utf-8') + ')',
        font=(PROGRAM_FONT, 25),
        justify='center'
    )
    title.pack(anchor='n', pady=(0, 50))

    input_label = tk.Label(
        master=frame,
        text='Please enter the text you wish to encrypt/decrypt:',
        font=(PROGRAM_FONT, 14),
        justify='center'
    )
    input_label.pack(anchor='n', pady=(0, 10))

    input_entry = tk.Entry(
        master=frame,
        font=(PROGRAM_FONT, 16),
        width=75,
        borderwidth=2,
    )
    input_entry.pack(pady=(0, 40))

    radio_code = tk.IntVar()

    radio_label = tk.Label(
        text='Select an option to perform:',
        font=(PROGRAM_FONT, 14)
    )
    radio_label.pack(pady=(0, 5))

    en = tk.Radiobutton(
        master=frame,
        text='Encrypt',
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=0
    )
    en.pack()

    de = tk.Radiobutton(
        master=frame,
        text='Decrypt',
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=1
    )
    de.pack(pady=(0, 50))

    def cmds():
        out = (input_entry.get())
        en_de = radio_code.get()
        if en_de == 'Encrypt':
            output.config(text=encrypt(out, key))
        else:
            output.config(text=decrypt(out, key))

    translate_button = tk.Button(
        master=frame,
        text='Translate!',
        font=(PROGRAM_FONT, 25),
        borderwidth=2,
        command=cmds
    )
    translate_button.pack(pady=(0, 75))

    output_label = tk.Label(
        master=frame,
        text='The output will be displayed below:',
        font=(PROGRAM_FONT, 14),
        justify='center',
    )
    output_label.pack(pady=(0, 5))

    output = tk.Label(
        text='. . .',
        master=frame,
        font=(PROGRAM_FONT, 16),
        borderwidth=2,
    )
    output.pack()

    # Atbash
    title = tk.Label(
        master=frame,
        text='Atbash',
        font=(PROGRAM_FONT, 25),
        justify='center'
    )
    title.pack(anchor='n', pady=(0, 50))

    input_label = tk.Label(
        master=frame,
        text='Please enter the text you wish to encrypt/decrypt:',
        font=(PROGRAM_FONT, 14),
        justify='center'
    )
    input_label.pack(anchor='n', pady=(0, 10))

    input_entry = tk.Entry(
        master=frame,
        font=(PROGRAM_FONT, 16),
        width=75,
        borderwidth=2,
    )
    input_entry.pack(pady=(0, 40))

    radio_code = tk.IntVar()

    radio_label = tk.Label(
        text='Select an option to perform:',
        font=(PROGRAM_FONT, 14)
    )
    radio_label.pack(pady=(0, 5))

    en = tk.Radiobutton(
        master=frame,
        text='Encrypt',
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=0
    )
    en.pack()

    de = tk.Radiobutton(
        master=frame,
        text='Decrypt',
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=1
    )
    de.pack(pady=(0, 50))

    def cmds():
        out = (input_entry.get())
        en_de = radio_code.get()
        if en_de == 'Encrypt':
            output.config(text=atbash_cipher(out))
        else:
            output.config(text=atbash_cipher(out))

    translate_button = tk.Button(
        master=frame,
        text='Translate!',
        font=(PROGRAM_FONT, 25),
        borderwidth=2,
        command=cmds
    )
    translate_button.pack(pady=(0, 75))

    output_label = tk.Label(
        master=frame,
        text='The output will be displayed below:',
        font=(PROGRAM_FONT, 14),
        justify='center',
    )
    output_label.pack(pady=(0, 5))

    output = tk.Label(
        text='. . .',
        master=frame,
        font=(PROGRAM_FONT, 16),
        borderwidth=2,
    )
    output.pack()

    # Letter to Number
    title = tk.Label(
        master=frame,
        text='Letter to Number',
        font=(PROGRAM_FONT, 25),
        justify='center'
    )
    title.pack(anchor='n', pady=(0, 50))

    input_label = tk.Label(
        master=frame,
        text='Please enter the text you wish to encrypt/decrypt:',
        font=(PROGRAM_FONT, 14),
        justify='center'
    )
    input_label.pack(anchor='n', pady=(0, 10))

    input_entry = tk.Entry(
        master=frame,
        font=(PROGRAM_FONT, 16),
        width=75,
        borderwidth=2,
    )
    input_entry.pack(pady=(0, 40))

    radio_code = tk.IntVar()

    radio_label = tk.Label(
        text='Select an option to perform:',
        font=(PROGRAM_FONT, 14)
    )
    radio_label.pack(pady=(0, 5))

    en = tk.Radiobutton(
        master=frame,
        text='Encrypt',
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=0
    )
    en.pack()

    de = tk.Radiobutton(
        master=frame,
        text='Decrypt',
        font=(PROGRAM_FONT, 16),
        variable=radio_code,
        value=1
    )
    de.pack(pady=(0, 50))

    def cmds():
        out = (input_entry.get())
        en_de = radio_code.get()
        if en_de == 'Encrypt':
            output.config(text=letter_to_number_encrypt(out))
        else:
            output.config(text=letter_to_number_decrypt(out))

    translate_button = tk.Button(
        master=frame,
        text='Translate!',
        font=(PROGRAM_FONT, 25),
        borderwidth=2,
        command=cmds
    )
    translate_button.pack(pady=(0, 75))

    output_label = tk.Label(
        master=frame,
        text='The output will be displayed below:',
        font=(PROGRAM_FONT, 14),
        justify='center',
    )
    output_label.pack(pady=(0, 5))

    output = tk.Label(
        text='. . .',
        master=frame,
        font=(PROGRAM_FONT, 16),
        borderwidth=2,
    )
    output.pack()

    return frame