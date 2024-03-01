from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style

root = Tk()
style = Style('cyborg')

# Create a frame for the sidebar
sidebar = ttk.Frame(root, style='primary.TFrame')
sidebar.pack(side=LEFT, fill=Y)

# Add widgets to the sidebar
label = ttk.Label(sidebar, text='Sidebar', style='info.TLabel')
label.pack(pady=10)

# Add entry fields with predefined text for each category
grocery_entry = ttk.Entry(sidebar, width=20)
grocery_entry.insert(0, 'Grocery')
grocery_entry.pack(pady=5)

electronics_entry = ttk.Entry(sidebar, width=20)
electronics_entry.insert(0, 'Electronics')
electronics_entry.pack(pady=5)

sports_entry = ttk.Entry(sidebar, width=20)
sports_entry.insert(0, 'Sports and Gym')
sports_entry.pack(pady=5)

furniture_entry = ttk.Entry(sidebar, width=20)
furniture_entry.insert(0, 'Furniture')
furniture_entry.pack(pady=5)

appliances_entry = ttk.Entry(sidebar, width=20)
appliances_entry.insert(0, 'Appliances')
appliances_entry.pack(pady=5)

social_activity_entry = ttk.Entry(sidebar, width=20)
social_activity_entry.insert(0, 'Social Activity')
social_activity_entry.pack(pady=5)

group_shopping_entry = ttk.Entry(sidebar, width=20)
group_shopping_entry.insert(0, 'Group Shopping')
group_shopping_entry.pack(pady=5)


root.mainloop()
