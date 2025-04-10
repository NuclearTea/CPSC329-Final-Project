import tkinter as tk
from src.gui.styles import PROGRAM_FONT


def crypto_tool_list(root, on_item_click):
    sidebar = tk.Frame(root, bg="#f0f0f0", bd=2, relief="solid", width=150)
    sidebar.pack(side="left", fill="y")

    sidebar.grid_rowconfigure((0, 1, 2, 3), weight=1)
    sidebar.grid_columnconfigure(0, weight=1)

    normal_bg = "#ffffff"
    hover_bg = "#e0e0e0"
    active_bg = "#d0d0d0"
    fg_color = "#333333"

    def on_enter(e):
        e.widget.config(bg=hover_bg)

    def on_leave(e):
        e.widget.config(bg=normal_bg)

    def determine_button_name(i):
        if i == 0:
            return "OTP hex <-> binary"
        if i == 1:
            return "Remove Duplicates"
        if i == 2:
            return "Encryption/Decryption"
        if i == 3:
            return "Caesar Cipher Translator"

    for i in range(4):
        button = tk.Button(
            sidebar,
            text=determine_button_name(i),
            font=(PROGRAM_FONT, 12, "bold"),
            bg=normal_bg,
            fg=fg_color,
            activebackground=active_bg,
            activeforeground=fg_color,
            bd=0,
            relief="flat",
            highlightthickness=0,
            command=lambda i=i: on_item_click(i),
            cursor="hand2",
            padx=10,
            pady=10,
        )
        button.grid(row=i, column=0, sticky="nsew", padx=10, pady=8)

        # Bind hover effects
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
