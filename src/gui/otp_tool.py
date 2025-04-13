import tkinter as tk
from tkinter import ttk
from Crypto.Random import get_random_bytes
from src.gui.styles import PROGRAM_FONT


def otp_encrypt(plaintext: str, key: bytes) -> bytes:
    data = plaintext.encode("utf-8")
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])


def component_1(parent):
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

    title = tk.Label(frame, text="OTP Encryptor", font=(PROGRAM_FONT, 25))
    title.pack(pady=(20, 10))

    input_label = tk.Label(frame, text="Enter plaintext:", font=(PROGRAM_FONT, 14))
    input_label.pack()
    input_entry = tk.Entry(frame, font=(PROGRAM_FONT, 16), width=75)
    input_entry.pack(pady=(0, 20))

    key_label = tk.Label(
        frame,
        text="Enter OTP key (leave empty to generate one):",
        font=(PROGRAM_FONT, 14),
    )
    key_label.pack()
    key_entry = tk.Entry(frame, font=(PROGRAM_FONT, 16), width=75)
    key_entry.pack(pady=(0, 20))

    format_label = tk.Label(frame, text="Output format:", font=(PROGRAM_FONT, 14))
    format_label.pack()

    output_format = tk.StringVar(value="hex")
    tk.Radiobutton(
        frame, text="Hex", font=(PROGRAM_FONT, 14), variable=output_format, value="hex"
    ).pack()
    tk.Radiobutton(
        frame,
        text="Binary",
        font=(PROGRAM_FONT, 14),
        variable=output_format,
        value="bin",
    ).pack()

    output_label = tk.Label(frame, text="Encrypted Output:", font=(PROGRAM_FONT, 14))
    output_label.pack(pady=(20, 5))

    output = tk.Text(frame, height=4, font=(PROGRAM_FONT, 16), wrap="word")
    output.insert("1.0", ". . .")
    output.config(state="disabled")
    output.pack(fill="x", padx=10)

    def translate():
        plaintext = input_entry.get()
        key_input = key_entry.get()

        if key_input:
            key = key_input.encode("utf-8")
        else:
            key = get_random_bytes(len(plaintext))

        encrypted = otp_encrypt(plaintext, key)

        if output_format.get() == "hex":
            encoded = encrypted.hex()
        else:
            encoded = "".join(format(b, "08b") for b in encrypted)

        output.config(state="normal")
        output.delete("1.0", tk.END)
        output.insert("1.0", encoded)
        output.config(state="disabled")

    translate_btn = tk.Button(
        frame, text="Encrypt", font=(PROGRAM_FONT, 18), command=translate
    )
    translate_btn.pack(pady=(10, 30))

    return container
