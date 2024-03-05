from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style

root = Tk()
style = Style('flatly')

# Create a frame for the navbar
navbar = ttk.Frame(root, style='primary.TFrame')
navbar.pack(side=TOP, fill=X)

# Create an entry field for the text in the navbar with placeholder effect
entry_field_navbar = ttk.Entry(navbar, width=20)
entry_field_navbar.insert(0, 'Proceed to Checkout')
entry_field_navbar.configure(state='readonly', foreground='black')
entry_field_navbar.pack(side=RIGHT, padx=20)
entry_field_navbar.pack(side=RIGHT, pady=20)

# Create a frame for the sidebar
sidebar = ttk.Frame(root, style='primary.TFrame')
sidebar.pack(side=LEFT, fill=Y)

# Add widgets to the sidebar

# Add entry fields with predefined text for each category set as disabled
categories = ['Grocery', 'Electronics', 'Sports and Gym', 'Furniture', 'Appliances', 'Social Activity', 'Group Shopping']

for category in categories:
    entry = ttk.Entry(sidebar, width=20)
    entry.insert(0, category)
    entry.configure(state='readonly')
    entry.pack(pady=15)

# Create a frame for products with an outline covering the remaining space
product_frame = ttk.Frame(root)
product_frame.pack(side=LEFT, fill=BOTH, expand=True)
product_frame.config(borderwidth=2, relief="solid")

# Add a title to the products frame
ttk.Label(product_frame, text="Products").pack(pady=15)

# Create 10 vertical subframes within the product frame with gray outline using pack

subframes = []
image_paths = []
for i in range(10):
    
    subframe = ttk.Frame(product_frame, borderwidth=2000, relief="solid")
    subframe.pack(side=TOP, fill=X)
    subframes.append(subframe)

    image_path = image_names[i]
    img = PhotoImage(file="WhatsApp Image 2024-03-05 at 14.32.38.jpeg")
    label = ttk.Label(subframe, image=img)
    label.image = img  # Keep a reference to the image to prevent garbage collection
    label.pack(pady=10)

# Load different images into each subframe (replace 'image_path_i' with actual image paths)

# Load different images into each subframe (replace 'image_path_i' with actual image paths)



root.mainloop()
