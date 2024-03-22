from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
import tkinter as tk


def create_navbar(root):
    navbar = ttk.Frame(root, style='primary.TFrame')
    navbar.pack(side=TOP, fill=X)

    entry_field_navbar = ttk.Entry(navbar, width=20, cursor="hand2")
    entry_field_navbar.insert(0, 'My Profile')
    entry_field_navbar.configure(state='readonly', foreground='black')
    entry_field_navbar.pack(side=RIGHT, padx=20)
    entry_field_navbar.pack(side=RIGHT, pady=20)


def create_sidebar(root):
    sidebar = ttk.Frame(root, style='primary.TFrame')
    sidebar.pack(side=LEFT, fill=Y)

    def on_furniture_click(event):  # Added root as a parameter
        new_window = tk.Toplevel()
        new_window.title("Furniture Page")

        product_frame = create_product_frame(new_window)

        image_paths = [
            # Add image paths for furniture products
            r"c:\Users\acer\Downloads\sofa.jpeg",
            r"c:\Users\acer\Downloads\bed.jpeg",
            r"c:\Users\acer\Downloads\cupboard.jpeg",
            r"c:\Users\acer\Downloads\diningtable.jpeg",
            r"c:\Users\acer\Downloads\table.jpeg",
            

            # Add more paths as needed
        ]

        texts = [
            "Furniture Product 1\n\nDescription of Product 1",
            "Furniture Product 2\n\nDescription of Product 2",
            "Furniture Product 3\n\nDescription of Product 3",
            "Furniture Product 4\n\nDescription of Product 4",
            "Furniture Product 5\n\nDescription of Product 5",
            # Add more texts as needed
        ]

        create_product_subframes(product_frame, image_paths, texts)

    categories = ['Grocery', 'Electronics', 'Sports and Gym', 'Furniture', 'Appliances', 'Social Activity',
                  'Group Shopping', 'Checkout']

    def on_category_click(event):
        print("Redirecting to category page:", event.widget.get())

    def on_grocery_click(event):
        open_new_page("Grocery Page")

    def on_sports_and_gym_click(event):
        open_new_page("Sports and Gym Page")

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

    ttk.Label(product_frame, text="Products", width=11, font=19).pack(pady=15)

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

        title_font = ('Arial', 16, 'bold')  # Professional font settings for title
        desc_font = ('Arial', 12)  # Professional font settings for description

        title_text = text.split('\n')[0]  # Extract title from text
        desc_text = '\n'.join(text.split('\n')[1:])  # Extract description from text

        title_label = ttk.Label(subframe, text=title_text, wraplength=200, justify='center', cursor="hand2",
                                font=title_font)
        title_label.bind("<Button-1>", on_product_click)  # Bind click event
        title_label.pack(pady=(5, 10))  # Add padding between title and description

        desc_label = ttk.Label(subframe, text=desc_text, wraplength=200, justify='center', cursor="hand2",
                               font=desc_font)
        desc_label.bind("<Button-1>", on_product_click)  # Bind click event
        desc_label.pack(pady=(0, 5))  # Add padding between description and Add to Cart button

        # Create Add to Cart button
        add_to_cart_button = ttk.Button(subframe, text="Add to Cart", command=lambda name=title_text: add_to_cart(name))
        add_to_cart_button.pack(side=BOTTOM, pady=10)  # Align to bottom of subframe


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
       r"Electronics\asus rog laptop.jpeg",
       r"Electronics\sony headphones.jpeg",
       r"Electronics\lg uhd tv.jpeg",
       r"Electronics\google pixel smartwatch.jpeg",
       r"Electronics\boat headphone.jpeg",
       
    ]

    texts = [
        # Add corresponding texts here
        "ASUS ROG Laptop\n\nDisplay size:15.00-inch\n\nRAM:8GB\n\nProcessor Core: i7\n\nGraphics:Nvidia GeForce GTX 950M\n\nWeight:2.70 kg",
        "Sony Headphones\n\nBattery Charge Time:Approx. 3hrs (Full charge)\n\nBattery Life:Max. 30 hrs (NC ON), Max. 200 hrs (NC Off)\n\nNoise Cancelling On/Off Switch:Yes\n\nHeadphone Type:Over-Ear\n",
        "LG UHD TV\n\nModel 65-inch NanoCell LED 4K HDR Smart TV (65SM9000)\n\nRelease date:July 2019\n\nDisplay Size:65 inch\n\nScreen Type:LED\n\nResolution Standard:4K",
        "Google Pixel Smartwatch\n\nDial Shape:Round\n\nDisplay Type:AMOLED\n\nRAM:2GB\n\nProcessor Name:Qualcomm 5100\n\nInternal Memory:32GB",
        "Boat Headphones\n\nColour:Green\n\nHeadphone Type:In-Ear\n\nMicrophone:Yes\n\nConnectivity:Wireless",
    ]

    create_product_subframes(product_frame, image_paths, texts)

    root.mainloop()


if __name__ == "__main__":
    main()
