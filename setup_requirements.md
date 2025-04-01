## 🛠 Setting Up Your Environment (Beginner Friendly)

### ✅ Before You Start

Make sure you have the following installed:

1. **Python 3.8+**

   - Download from: https://www.python.org/downloads/
   - ✅ Be sure to **check the box to "Add Python to PATH"** during installation (on Windows).

2. **Git** (to download the code from GitHub)

   - Download from: https://git-scm.com/downloads
   - On Windows, install with default options.
   - On macOS/Linux, it may already be installed. You can check with:
     ```bash
     git --version
     ```

3. **A Code Editor (Recommended: VS Code)**
   - Download from: https://code.visualstudio.com/
   - After installing, also install the **Python extension** from the Extensions tab.

---

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
cd src
python main.py
```

You should see a window pop up saying **"Hello, Tkinter!"**

---

## 🧰 Base Tkinter Project Setup

### Create `main.py`

```python
from gui.main_window import create_main_window

if __name__ == "__main__":
    window = create_main_window()
    window.mainloop()
```

### Create `gui/main_window.py`

```python
import tkinter as tk

def create_main_window():
    window = tk.Tk()
    window.title("Tkinter App")
    window.geometry("400x300")

    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack(pady=20)

    return window
```

### Create `logic/example_logic.py`

```python
def example_function():
    return "This is an example logic function."
```

### Optional: Add a basic test

`tests/test_example.py`

```python
from logic.example_logic import example_function

def test_example_function():
    assert example_function() == "This is an example logic function."
```

You're ready to go! 🎉
