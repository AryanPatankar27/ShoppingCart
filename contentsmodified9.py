from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
import tkinter as tk

def create_navbar(root):
    navbar = ttk.Frame(root, style='primary.TFrame')
    navbar.pack(side=TOP, fill=X)
    
    entry_field_navbar = ttk.Entry(navbar, width=20,cursor="hand2")
    entry_field_navbar.insert(0, 'My Profile')
    entry_field_navbar.configure(state='readonly', foreground='black')
    entry_field_navbar.pack(side=RIGHT, padx=20)
    entry_field_navbar.pack(side=RIGHT, pady=20)

def create_sidebar(root):
    sidebar = ttk.Frame(root, style='primary.TFrame')
    sidebar.pack(side=LEFT, fill=Y)
    
    categories = ['Grocery', 'Electronics', 'Sports and Gym', 'Furniture', 'Appliances', 'Social Activity', 'Group Shopping','Checkout']
    
    def on_category_click(event):
        print("Redirecting to category page:", event.widget.get())
    
    def on_furniture_click(event):
        open_new_page("Furniture Page")

    def on_grocery_click(event):
        open_new_page("Grocery Page")

    def on_sports_and_gym_click(event):
        open_new_page("Sports and Gym Page")
    
    def on_furniture_click(event):
        open_new_page("Furniture Page")
    

    def on_appliances_click(event):
        open_new_page("Appliances Page")

    def on_social_activity_click(event):
        open_new_page("Social Activity Page")

    def on_group_shopping_click(event):
        open_new_page("Group Shopping Page")

    for category in categories:
        entry = ttk.Entry(sidebar, width=20, cursor="hand2")
        entry.insert(0, category)
        entry.configure(state='readonly')
        if category == 'Furniture':
            entry.bind("<Button-1>", on_furniture_click)
        elif category == 'Grocery':
            entry.bind("<Button-1>", on_grocery_click)
        elif category == 'Sports and Gym':
            entry.bind("<Button-1>", on_sports_and_gym_click)
        elif category == 'Appliances':
            entry.bind("<Button-1>", on_appliances_click)
        elif category == 'Social Activity':
            entry.bind("<Button-1>", on_social_activity_click)
        elif category == 'Group Shopping':
            entry.bind("<Button-1>", on_group_shopping_click)
        else:
            entry.bind("<Button-1>", on_category_click)
        entry.pack(pady=15)

def open_new_page(page_name):
    new_window = tk.Toplevel()
    new_window.title(page_name)

    # Maximize the window
    new_window.attributes('-zoomed', True)

    # Example widget in the new page
    label = ttk.Label(new_window, text=f"Welcome to {page_name}!")
    label.pack(pady=20)

def create_product_frame(root):
    product_frame = ttk.Frame(root)
    product_frame.pack(side=LEFT, fill=BOTH, expand=True)
    product_frame.config(borderwidth=2, relief="solid")
    
    ttk.Label(product_frame, text="Products").pack(pady=15)

    return product_frame

def create_product_subframes(parent_frame, image_paths, texts):
    def on_product_click(event):
        print("Redirecting to product page:", event.widget.cget("text"))
    
    for i, (image_path, text) in enumerate(zip(image_paths, texts)):
        subframe = ttk.LabelFrame(parent_frame, width=500, height=200)
        subframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        
        img = Image.open(image_path)
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        
        subframe_label = ttk.Label(subframe, image=img)
        subframe_label.image = img
        subframe_label.pack(pady=5)
        
        title_font = ('Montserrat', 16)
        desc_font = ('Lato', 12)
        
        title_text = text.split('\n')[0]  # Extract title from text
        desc_text = '\n'.join(text.split('\n')[1:])  # Extract description from text
        
        title_label = ttk.Label(subframe, text=title_text, wraplength=200, justify='center', cursor="hand2", font=title_font)
        title_label.bind("<Button-1>", on_product_click)  # Bind click event
        title_label.pack(pady=5)
        
        desc_label = ttk.Label(subframe, text=desc_text, wraplength=200, justify='center', cursor="hand2", font=desc_font)
        desc_label.bind("<Button-1>", on_product_click)  # Bind click event
        desc_label.pack(pady=5)

        # Create Add to Cart button
        add_to_cart_button = ttk.Button(subframe, text="Add to Cart", command=lambda: add_to_cart(title_text))
        add_to_cart_button.pack(pady=5)

def add_to_cart(product_name):
    print(f"Added '{product_name}' to cart")

def main():
    root = tk.Tk()
    style = Style('flatly')

    create_navbar(root)
    create_sidebar(root)
    
    product_frame = create_product_frame(root)

    image_paths = [
        # Add your image paths here
       r"C:\Users\Admin\Downloads\asus rog laptop.jpeg",
       r"C:\Users\Admin\Downloads\sony.jpeg",
       r"C:\Users\Admin\Downloads\lg uhd tv.jpeg",
       r"C:\Users\Admin\Downloads\iphone 15.jpeg",
       r"C:\Users\Admin\Downloads\google pixel smartwatch.jpeg",
       r"C:\Users\Admin\Downloads\boat headphones.jpeg",
    ]

    texts = [
        # Add corresponding texts here
        "ASUS ROG Laptop\nDisplay size:15.00-inch\nRAM:8GB\nProcessor Core: i7\nGraphics:Nvidia GeForce GTX 950M\nWeight:2.70 kg",
        "Sony Headphones\nBATTERY CHARGE TIME:Approx. 3 hours (Full charge)\nBATTERY LIFE (WAITING TIME):Max. 30 hours (NC ON), Max. 200 hours (NC OFF)\nNOISE CANCELLING ON/OFF SWITCH:Yes\nHeadphone Type:Over-Ear\n",
        "LG UHD TV\nModel	65-inch NanoCell LED 4K HDR Smart TV (65SM9000)\nRelease date:July 2019\nDisplay Size:65 inch\nScreen Type:LED\nResolution Standard:4K",
        "iPhone 15\nDisplay:6.10-inch (1179x2556)\n Processor:Apple A16 Bionic\nFront Camera:12MP\nRear Camera:48MP + 12MP\nRAM:6GB\nStorage:128GB, 256GB, 512GB\nOS:iOS 17",
        "Google Pixel Smartwatch\nDial Shape:Round\nDisplay Type:AMOLED\nRAM:2GB\nProcessor Name:Qualcomm 5100\nInternal Memory:32GB",
        "Boat Headphones\nColour:Green\nHeadphone Type:In-Ear\nMicrophone:Yes\nConnectivity:Wireless",
    ]

    create_product_subframes(product_frame, image_paths, texts)

    root.mainloop()

if __name__ == "__main__":
   main()
