# 🔐 OTP Component Design References

This document outlines key implementation decisions made in the `component_otp` Tkinter GUI and includes official documentation or reference links to support each choice.

---

## 📦 Core Concepts

### 1. `tk.Text` for Selectable Output

- **Reason**: `Label` widgets do not allow text selection. `Text` widgets do, making it possible to copy encrypted output.
- **Reference**: [Tkinter Text Widget – Python Docs](https://docs.python.org/3/library/tkinter.html#text-widgets)

---

### 2. `tk.Canvas` + Scrollable Frame

- **Reason**: Tkinter does not provide native scrolling for `Frame`. A `Canvas` with a scrollable window is a common workaround.
- **Reference**:
  - [Tkinter Scrollable Frames – Teclado Blog](https://blog.teclado.com/tkinter-scrollable-frames/)

---

### 3. `get_random_bytes()` from PyCryptodome

- **Reason**: Secure, cryptographically strong random bytes for OTP key generation when not provided by the user.
- **Reference**: [PyCryptodome – Crypto.Random.get_random_bytes](https://pycryptodome.readthedocs.io/en/latest/src/random/random.html#Crypto.Random.get_random_bytes)

---

### 4. OTP via XOR

- **Reason**: One-Time Pad encryption uses XOR between plaintext bytes and key bytes.
- **Reference**:
  - [Python Built-in `bytes()`](https://docs.python.org/3/library/functions.html#bytes)
  - [Real Python – Bitwise XOR](https://realpython.com/python-bitwise-operators/#bitwise-xor)

---

### 5. Binary Output Formatting

- **Code**: `format(b, '08b')`
- **Reason**: Converts each encrypted byte to a zero-padded 8-bit binary string.
- **Reference**: [Python `format()` Function](https://docs.python.org/3/library/functions.html#format)

---

## 🧩 GUI Behavior

### 6. `tk.StringVar` / `tk.IntVar`

- **Reason**: Used to bind values to radio buttons for selecting output format and encrypt/decrypt mode.
- **Reference**:
  - [TkDocs – Control Variables](https://tkdocs.com/tutorial/complex.html#variables)
  - [Tkinter Variable Classes – Python Docs](https://docs.python.org/3/library/tkinter.html#control-variables)

---

### 7. `enumerate()` for Indexed XOR

- **Reason**: Needed to access both the byte and its index to align key/plaintext for XOR.
- **Reference**: [Python `enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)

---

### 8. Use of `pack()` with Padding

- **Reason**: Simple and readable layout logic for stacking widgets vertically with space between them.
- **Reference**:
  - [TkDocs – Geometry Managers](https://www.tutorialspoint.com/python/tk_pack.htm)
  - [TkDocs – `grid()` vs `pack()`](https://tkdocs.com/tutorial/grid.html)
