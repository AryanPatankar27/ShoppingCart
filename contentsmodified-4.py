from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

def create_navbar(root):
    navbar = ttk.Frame(root, style='primary.TFrame')
    navbar.pack(side=TOP, fill=X)
    
    entry_field_navbar = ttk.Entry(navbar, width=20)
    entry_field_navbar.insert(0, 'Proceed to Checkout')
    entry_field_navbar.configure(state='readonly', foreground='black')
    entry_field_navbar.pack(side=RIGHT, padx=20)
    entry_field_navbar.pack(side=RIGHT, pady=20)

def create_sidebar(root):
    sidebar = ttk.Frame(root, style='primary.TFrame')
    sidebar.pack(side=LEFT, fill=Y)
    
    categories = ['Grocery', 'Electronics', 'Sports and Gym', 'Furniture', 'Appliances', 'Social Activity', 'Group Shopping']
    
    def on_category_click(event):
        print("Redirecting to category page:", event.widget.get())
    
    for category in categories:
        entry = ttk.Entry(sidebar, width=20, cursor="hand2")
        entry.insert(0, category)
        entry.configure(state='readonly')
        entry.bind("<Button-1>", on_category_click)  # Bind click event
        entry.pack(pady=15)

def create_product_frame(root):
    product_frame = ttk.Frame(root)
    product_frame.pack(side=LEFT, fill=BOTH, expand=True)
    product_frame.config(borderwidth=2, relief="solid")
    
    ttk.Label(product_frame, text="Products").pack(pady=15)

def create_product_subframes(parent_frame, image_paths, texts):
    def on_product_click(event):
        print("Redirecting to product page:", event.widget.cget("text"))
    
    for i, (image_path, text) in enumerate(zip(image_paths, texts)):
        subframe = ttk.LabelFrame(parent_frame, width=300, height=100)
        subframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        
        img = Image.open(image_path)
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        
        subframe_label = ttk.Label(subframe, image=img)
        subframe_label.image = img
        subframe_label.pack(pady=5)
        
        text_label = ttk.Label(subframe, text=text, wraplength=200, justify='center', cursor="hand2")
        text_label.bind("<Button-1>", on_product_click)  # Bind click event
        text_label.pack(pady=5)

def create_additional_subframes(parent_frame):
    for i in range(4):
        subframe_below = ttk.LabelFrame(parent_frame, text="Subframe Below {}".format(i+1), width=300, height=200)
        subframe_below.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

def main():
    root = Tk()
    style = Style('flatly')

    create_navbar(root)
    create_sidebar(root)
    
    product_frame = create_product_frame(root)

    image_paths = [
        # Add your image paths here
            r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.38.jpeg",
    r"C:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (1).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (4).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (5).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (7).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39 (9).jpeg",
    r"c:\Users\Admin\Desktop\shoopping cart images\WhatsApp Image 2024-03-05 at 14.32.39.jpeg"
    ]

    texts = [
        # Add corresponding texts here
        "Sony Headphones",
    "Dell Laptop",
    "LG TV",
    "iPhone 15",
    "Firebolt Smartwatch",
    "ASUS ROG Laptop",
    "Boat Headphones"
    ]

    create_product_subframes(product_frame,image_paths,texts)

    line2_frame = ttk.Frame(product_frame)
    line2_frame.pack(side=TOP, fill=X)

    

    create_additional_subframes(line2_frame)

    root.mainloop()

if __name__ == "__main__":
   main()