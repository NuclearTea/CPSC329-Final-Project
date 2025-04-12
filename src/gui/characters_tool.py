import tkinter as tk
from src.gui.styles import PROGRAM_FONT
from src.logic.remove_duplicates_logic import remove_duplicates, duplicate_characters


def component_2(parent):
    frame = tk.Frame(parent, bg="white")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    explanation = """
This tool helps modify text strings by either removing or duplicating specified characters.

How to use:
1. Enter your input text
2. List characters to process (comma-separated)
3. Choose operation (remove/duplicate)
4. Click Process

Application in cryptography:
- Cleaning plaintext by removing special characters
- Creating patterns by duplicating specific characters
- Preparing text for other cryptographic operations
"""
    explanation_label = tk.Label(
        frame,
        text=explanation.strip(),
        font=(PROGRAM_FONT, 12),
        bg="white",
        justify="left",
        wraplength=600
    )
    explanation_label.pack(anchor="w", pady=(0, 20))

    # Input String
    input_label = tk.Label(frame, text="Input String:", font=(PROGRAM_FONT, 12), bg="white")
    input_label.pack(anchor="w")

    input_entry = tk.Entry(frame, font=(PROGRAM_FONT, 12), width=50)
    input_entry.pack(fill="x", padx=10, pady=5)

    # Characters to Process
    chars_label = tk.Label(
        frame,
        text="Characters to process (comma-separated):",
        font=(PROGRAM_FONT, 12),
        bg="white"
    )
    chars_label.pack(anchor="w", pady=(10, 0))

    chars_entry = tk.Entry(frame, font=(PROGRAM_FONT, 12), width=50)
    chars_entry.pack(fill="x", padx=10, pady=5)

    # Operation Selection
    operation_var = tk.StringVar(value="remove")

    radio_frame = tk.Frame(frame, bg="white")
    radio_frame.pack(anchor="w", pady=(10, 0))

    tk.Radiobutton(
        radio_frame,
        text="Remove Characters",
        variable=operation_var,
        value="remove",
        font=(PROGRAM_FONT, 12),
        bg="white",
        activebackground="white"
    ).pack(side="left", padx=(0, 20))

    tk.Radiobutton(
        radio_frame,
        text="Duplicate Characters",
        variable=operation_var,
        value="duplicate",
        font=(PROGRAM_FONT, 12),
        bg="white",
        activebackground="white"
    ).pack(side="left")

    # Process Button
    def process_input():
        # Get values from user input
        input_str = input_entry.get()
        raw_chars = chars_entry.get()

        # Clean and validate characters
        chars = [c.strip() for c in raw_chars.split(',') if c.strip()]
        valid_chars = [c for c in chars if len(c) == 1]

        # Remove duplicate characters in specification
        unique_chars = list(set(valid_chars))

        # Perform operation
        if operation_var.get() == "remove":
            result = remove_duplicates(input_str, unique_chars)
        else:
            result = duplicate_characters(input_str, unique_chars)

        # Display result
        result_label.config(text=f"Result: {result}")

    process_btn = tk.Button(
        frame,
        text="Process",
        font=(PROGRAM_FONT, 12, "bold"),
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        command=process_input
    )
    process_btn.pack(pady=20)

    # Result Display
    result_label = tk.Label(
        frame,
        text="Result will appear here",
        font=(PROGRAM_FONT, 12),
        bg="white",
        wraplength=500
    )
    result_label.pack(fill="x", padx=10, pady=5)

    return frame