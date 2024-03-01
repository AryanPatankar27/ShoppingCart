from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
root = tk.Tk()
root.title("Navbar Example")

# Create a style object
style = Style(theme="flatly")

# Create a navbar frame
navbar = ttk.Frame(root)
navbar.pack(side="top", fill="x")

# Add buttons to the navbar
home_button = ttk.Button(navbar, text="Home")
home_button.pack(side="left", padx=10, pady=5)

about_button = ttk.Button(navbar, text="About")
about_button.pack(side="left", padx=10, pady=5)

contact_button = ttk.Button(navbar, text="Contact")
contact_button.pack(side="left", padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()