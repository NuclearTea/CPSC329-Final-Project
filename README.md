# Directory structure (not code)

```
project-root/
│
├── src/
│ ├── main.py
│ ├── gui/
│ │ └── main_window.py
│ └── logic/
│ └── example_logic.py
│
├── tests/
│ └── test_example.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── setup_instructions.md
```

## ▶️ How to Run

### Ensure that you have 1 of the following

- PyCharm
- Python version ~3.13 (we used this but I don't think it needs to be this exactly, could be close)

If using PyCharm, simply run the main.py file and it should work!

If using the command line do the following:

### Step 1: Clone the Repository

```bash
git clone https://github.com/NuclearTea/CPSC329-Final-Project.git
cd CPSC329-Final-Project
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Environment

```bash
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

You should see the environment name (e.g. `(venv)`) at the beginning of your terminal prompt.

---

### Step 4: Install Python Packages

```bash
pip install -r requirements.txt
```

If you don’t see any output or it installs very quickly, that’s okay — this project uses mostly built-in libraries.

---

### Step 5: Run the App

```bash
python -m src.main
```

## 🧪 How to Run Tests

```bash
pytest
```

---

## How it works and how to interact with it

## Cryptography Tools Application

Overview
This project is a beginner-friendly cryptography toolkit that helps users explore different ways of encrypting and decrypting messages. It includes four main tools, all accessible through a simple interface where you can type text, click buttons, and get instant results.

Included Tools:

-Caesar Cipher Translator
-AES, Atbash, and Letter-to-Number Encryption
-Character Duplication/Removal Tool
-OTP Output in Hex or Binary

1. Caesar Cipher Translator

What it does:
Encrypts and decrypts messages by shifting each letter forward or backward in the alphabet.

How it works:
You enter a word or sentence and a number (called the key).
The tool shifts each letter by that number.
For example, with a key of 3:
A becomes D, B becomes E, and so on.
To decrypt, the tool shifts letters backward.

Example:
Input: HELLO, Key: 3
Encrypted: KHOOR
Decrypted: HELLO

2. AES, Atbash, and Letter-to-Number Encryption

What it does:
Gives you three different ways to secure your message.

AES:
Uses a strong key-based system to lock and unlock your message.
It’s widely used in modern applications.
You just enter your text and a key, and it does the rest.

Atbash Cipher:
A classic cipher that flips the alphabet.
For example, A becomes Z, B becomes Y, etc.
Simple and fun to use!

Example:
Input: HELLO
Output: SVOOL

Letter-to-Number:
Converts each letter into its number position in the alphabet. A = 1, B = 2, ..., Z = 26

Example:
Input: ABC
Output: 1 2 3

3. Character Duplication/Removal Tool
   What it does:
   You give it a sentence and a list of characters. It either duplicates or removes those characters.

Example Sentence:
The fox jumps high.
If you choose to duplicate h and o:
Output: Thhe foox jumps hhigh.

If you choose to remove h and o:
Output: Te fx jumps igh.

Why it’s useful:
Perfect for experimenting with how small changes can affect a string, especially in encoding systems.

4. OTP Output Display (Hex or Binary)
   What it does:
   Encrypts a message using a One-Time Pad and lets you see the result in either hexadecimal or binary.

How it works:
You enter a message and a secret key of the same length.
The tool encrypts the message using XOR.
Then you choose how to view it—hex or binary.

Example:
Plaintext: HELLO
Key: XMCKL
Output (Hex): 1a0c0f0f0a
Output (Binary): 00011010 00001100 00001111 00001111 00001010

Why it matters:
It helps you understand how encrypted data is stored and transferred digitally.
