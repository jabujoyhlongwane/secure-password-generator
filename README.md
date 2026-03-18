
# 🔐 Secure Password Generator

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)

A modern, secure password generator with a clean graphical user interface. Generate strong, cryptographically secure passwords with customizable options. Built with Python and Tkinter.

---

## 📸 Screenshot

*[Screenshot will be added here once I run the app]*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎚️ **Adjustable Length** | Choose password length from 4 to 64 characters |
| 🔤 **Character Options** | Toggle uppercase, lowercase, numbers, and symbols |
| 🔒 **Cryptographically Secure** | Uses Python's `secrets` module for true randomness |
| 📋 **One-Click Copy** | Copy generated passwords to clipboard instantly |
| 🎨 **Modern UI** | Clean, dark-themed interface |
| ⚡ **Instant Generation** | Generate new passwords in real-time |

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher installed on your computer
- pip (usually comes with Python)

### Steps to Install and Run

1. **Download the project**
   ```bash
   git clone https://github.com/yourusername/secure-password-generator.git
   cd secure-password-generator
2. **Install the required package**

 ```bash 
pip install pyperclip
```
3. **Run the application**

```bash
python ui.py
```

🎯 How to Use
Step-by-Step Guide
Launch the app

```bash
python ui.py
```
Set password length

Use the up/down arrows to select length (4-64 characters)

Default is 12 characters

Choose character types

✅ Check Uppercase for A-Z

✅ Check Lowercase for a-z

✅ Check Numbers for 0-9

✅ Check Symbols for !@#$%^&*

Generate password

Click the "Generate Secure Password" button

Your password appears in the green text box

Copy to clipboard

Click "Copy to Clipboard" button

Password is now ready to paste anywhere

Example
text
Length: 16
Options: ✅ Uppercase ✅ Lowercase ✅ Numbers ✅ Symbols
Generated: K9#mP2$qR8!vL5@n
📁 Project Structure
text
secure-password-generator/
│
├── ui.py              # The graphical interface (GUI)
├── generator.py       # Password generation logic
├── requirements.txt   # List of required packages
└── README.md          # This file
File Descriptions
File	Purpose
ui.py	Contains all the window, buttons, and interface code
generator.py	Has the secure password generation function
requirements.txt	Lists pyperclip as the only dependency
README.md	Project documentation (you're reading it)
🔒 Security Details
This password generator is truly secure because:

Uses secrets module - Not random which is predictable

Local generation - No internet connection needed

No storage - Passwords aren't saved anywhere

High entropy - All character sets ensure maximum randomness

Why secrets is better than random:
python
## ❌ Don't use this (predictable)
import random
password = random.choice(characters)

## ✅ This is secure (cryptographically random)
import secrets
password = secrets.choice(characters)
🛠️ Technologies Used
Python 3.x - Core programming language

Tkinter - GUI framework (built into Python)

Pyperclip - Cross-platform clipboard functionality

Secrets Module - Cryptographic random number generation

❓ Frequently Asked Questions
Q: Is this really secure?
A: Yes! It uses Python's secrets module which is designed for passwords and cryptographic purposes.

Q: Can I save my passwords?
A: No, this app intentionally doesn't save passwords for security reasons.

Q: Why is there only one dependency?
A: Tkinter comes with Python, and we only need pyperclip for clipboard functionality.

Q: Will this work on Mac/Linux?
A: Yes! Python and Tkinter work on all major operating systems.

## 🚀 Future Updates (Coming Soon)
Password strength meter

Dark/Light theme toggle

Multiple passwords at once

Export to encrypted file

Password history (encrypted)

## 🤝 Contributing
### Contributions are welcome! Here's how:

Fork the repository

Create a new branch (git checkout -b feature/improvement)

Make your changes

Commit (git commit -m 'Add feature')

Push (git push origin feature/improvement)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see below:

text
MIT License

Copyright ©️ 2026 Jabu Hlongwane

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
📧 Contact & Support
Created by: Jabu Hlongwane

📧 Email: Available on my LinkedIn

💼 LinkedIn: (https://www.linkedin.com/in/jabujoyhlongwane/)

Project Link: https://github.com/jabujoyhlongwane/secure-password-generator

⭐ Show Your Support
If you found this project helpful, please give it a ⭐ on GitHub!

https://img.shields.io/github/stars/jabujoyhlongwane/secure-password-generator?style=social

Made with 🔒 and Python
