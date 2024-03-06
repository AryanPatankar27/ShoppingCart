from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

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

# Create 4 rectangular subframes in one line
line1_frame = ttk.Frame(product_frame)
line1_frame.pack(side=TOP, fill=X)

# List of image paths and corresponding texts
image_paths = [
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.38.jpeg",
    r"C:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (1).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (4).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (5).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (7).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (9).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39.jpeg"
]

texts = [
    "Sony Headphones",
    "Dell Laptop",
    "LG TV",
    "iPhone 15",
    "Firebolt Smartwatch",
    "ASUS ROG Laptop",
    "Boat Headphones"
]

# Iterate over image paths and create subframes with images and text
for i, (image_path, text) in enumerate(zip(image_paths, texts)):
    subframe = ttk.LabelFrame(line1_frame, width=300, height=200)
    subframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
    img = Image.open(image_path)
    img = img.resize((150, 150))  # Resize image to fit the subframe
    img = ImageTk.PhotoImage(img)
    subframe_label = ttk.Label(subframe, image=img)
    subframe_label.image = img  # Keep a reference to prevent garbage collection
    subframe_label.pack(pady=5)
    text_label = ttk.Label(subframe, text=text, wraplength=200, justify='center')
    text_label.pack(pady=5)

# Create 4 rectangular subframes below the first set
line2_frame = ttk.Frame(product_frame)
line2_frame.pack(side=TOP, fill=X)

image_paths2 = [
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (2).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (8).jpeg",
   
]
texts2 = [
    "Sony Headphones",
    "Dell Laptop",
]

for i in range(4):
    subframe_below = ttk.LabelFrame(line2_frame, text="Subframe Below {}".format(i+1), width=300, height=200)
    subframe_below.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
    ttk.Label(subframe_below).pack(pady=15)


root.mainloop()
