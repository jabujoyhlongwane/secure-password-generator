# ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip # This library will let us copy to clipboard
from generator import generate_password

# --- Functions for UI actions ---
def on_generate():
    """Gets options from UI and calls the password generator."""
    try:
        # Get the length from the spinbox
        length = int(length_var.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be positive.")
            return

        # Get the boolean values from checkboxes
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        # Call the generator function from our logic file
        password = generate_password(
            length=length,
            use_uppercase=use_upper,
            use_lowercase=use_lower,
            use_numbers=use_digits,
            use_symbols=use_symbols
        )

        # Display the password in the entry field
        password_var.set(password)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_copy():
    """Copies the generated password to the clipboard."""
    password = password_var.get()
    if password and "Error" not in password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# --- Setup the main window ---
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("500x400")
root.resizable(False, False) # Make window fixed size
root.configure(bg='#2b2b2b') # Set a dark background

# Use a modern theme for ttk widgets
style = ttk.Style()
style.theme_use('clam')
# Configure colors for the modern look
style.configure('TLabel', background='#2b2b2b', foreground='white', font=('Segoe UI', 10))
style.configure('TCheckbutton', background='#2b2b2b', foreground='white', font=('Segoe UI', 10))
style.configure('TButton', font=('Segoe UI', 10, 'bold'), borderwidth=0)
style.map('TButton', background=[('active', '#4a4a4a')])

# --- Variables to hold UI state ---
length_var = tk.IntVar(value=12)  # Default length 12
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar() # This will hold the generated password

# --- UI Layout ---

# Title Label
title_label = ttk.Label(root, text="Password Generator", font=('Segoe UI', 18, 'bold'))
title_label.pack(pady=20)

# Frame for length selection
length_frame = ttk.Frame(root)
length_frame.pack(pady=10)
ttk.Label(length_frame, text="Password Length:", font=('Segoe UI', 11)).pack(side=tk.LEFT, padx=10)
# Use Spinbox to select length
length_spinbox = tk.Spinbox(length_frame, from_=4, to_=64, textvariable=length_var, width=5,
                             font=('Segoe UI', 11), bg='#3c3c3c', fg='white', bd=0)
length_spinbox.pack(side=tk.LEFT)

# Frame for checkboxes (character types)
options_frame = ttk.Frame(root)
options_frame.pack(pady=20)

# Create a 2x2 grid for checkboxes using grid layout inside the frame
upper_check = ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=upper_var)
upper_check.grid(row=0, column=0, sticky='w', padx=20, pady=5)

lower_check = ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=lower_var)
lower_check.grid(row=0, column=1, sticky='w', padx=20, pady=5)

digits_check = ttk.Checkbutton(options_frame, text="Numbers (0-9)", variable=digits_var)
digits_check.grid(row=1, column=0, sticky='w', padx=20, pady=5)

symbols_check = ttk.Checkbutton(options_frame, text="Symbols (!@#)", variable=symbols_var)
symbols_check.grid(row=1, column=1, sticky='w', padx=20, pady=5)

# Frame for the generate button
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)
generate_btn = ttk.Button(button_frame, text="Generate Secure Password", command=on_generate)
generate_btn.pack()

# Frame for displaying the generated password
display_frame = ttk.Frame(root)
display_frame.pack(pady=20)
ttk.Label(display_frame, text="Generated Password:", font=('Segoe UI', 11)).pack()
# Use an Entry widget to show the password (makes it easy to select)
password_entry = tk.Entry(display_frame, textvariable=password_var, font=('Consolas', 12),
                          width=30, justify='center', state='readonly',
                          bg='#3c3c3c', fg='#00ff7f', bd=2, relief='flat')
password_entry.pack(pady=5)

# Frame for the copy button
copy_frame = ttk.Frame(root)
copy_frame.pack(pady=10)
copy_btn = ttk.Button(copy_frame, text="Copy to Clipboard", command=on_copy)
copy_btn.pack()

# Footer label
footer_label = ttk.Label(root, text="🔐 Uses cryptographically secure randomness.", font=('Segoe UI', 8))
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start the UI event loop
if __name__ == "__main__":
    root.mainloop()