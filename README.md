---

## PyPass — Password Generator

> *Simple to use. Hard to crack. Free forever.*

**PyPass** is a free, fully offline, terminal-based password generator built in Python by **Sudipta Sunder**, a passionate teenage developer. It generates strong, readable, word-based passwords using a curated vocabulary and true randomness — no internet, no accounts, no cost.

---

### 🔐 How Passwords Are Generated

PyPass builds passwords by combining words from its built-in word collections, separated by random characters like `-`, `*`, `_`, and more. Python's `random` module shuffles everything — words, separators, and structure — on every single run, ensuring no two passwords are ever the same.

Choose from two word collections based on your needs:

| Collection | Words | Best For |
|------------|-------|----------|
| 📖 Common Words | 1,000 | Memorable, everyday passwords |
| 📚 Rare English Words | 2,500 | High-entropy, harder-to-guess passwords |

---

### ⚙️ Features

- 🌐 **Fully Offline** — Runs entirely on your machine. No data is ever sent over the internet
- 🔒 **Stealth Mode** — A privacy-first toggle that, when enabled:
  - Prevents passwords from being **copied to the clipboard**
  - Prevents passwords from being **saved to any text file**
  - Leaves **zero trace** of your generated passwords on disk
- 🎲 **True Randomness** — Every password is freshly shuffled using Python's `random` module
- 🖥️ **Clean Terminal UI** — Colorful, readable interface powered by `colorama`
- 💸 **Completely Free** — No subscriptions, no sign-ups, open source

---

### 🛠️ Built With

| Module | Purpose |
|--------|---------|
| `random` | Shuffles words and separators for unpredictable generation |
| `colorama` | Colored terminal output for a clean UI |
| `time` | Controls timing and display flow |
| `os` | File and system operations |
| `sys` | System-level controls |
| `webbrowser` | Opens links directly from the terminal for viewing my github profile |

---

### 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/sudiptasunder/pypass.git

# Navigate into the folder
cd PyPass

# Install dependencies
pip install colorama

# Run the program
python main.py
```

---

### 📁 Project Structure

```
PyPass/
│
├── pypass.py               # Entry point
├── stealth_mode.txt      # Stores stealth mode preference
├── passwords.txt         # Saved passwords (bypassed in Stealth Mode)
└── wordlist.py      # 2,500 rare English words + 1000 common English words
```

---

### ⚠️ Disclaimer

PyPass is an independent, open-source project developed for educational and personal use. Always use strong, unique passwords for sensitive accounts and consider a dedicated password manager for critical credentials.

---

### 👨‍💻 Developer

Made with ❤️ by **Sudipta Sunder**
A teenage Python developer from India, building practical tools for real-world problems.

---

> ⭐ If you find this project useful, consider leaving a star on the repo!
