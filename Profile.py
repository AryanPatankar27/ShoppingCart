import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def open_profile_page():
    profile_window = tk.Toplevel(root)
    profile_window.title("My Profile")

    # Widgets for profile page
    ttk.Label(profile_window, text="My Profile", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    # Example profile entries
    ttk.Label(profile_window, text="Profile Picture").pack()
    ttk.Label(profile_window, text="Username: JohnDoe").pack()
    ttk.Label(profile_window, text="Email: johndoe@example.com").pack()
    
    ttk.Separator(profile_window, orient="horizontal").pack(fill="x", pady=10)
    
    ttk.Label(profile_window, text="Address Information", font=("Helvetica", 12, "bold")).pack()
    ttk.Label(profile_window, text="Shipping Address: 123 Main St, City, Country").pack()
    ttk.Label(profile_window, text="Billing Address: 456 Broad St, City, Country").pack()

    ttk.Separator(profile_window, orient="horizontal").pack(fill="x", pady=10)

    ttk.Label(profile_window, text="Payment Methods", font=("Helvetica", 12, "bold")).pack()
    ttk.Label(profile_window, text="Credit Card: **** **** **** 1234").pack()
    ttk.Label(profile_window, text="PayPal: johndoe@example.com").pack()

    ttk.Separator(profile_window, orient="horizontal").pack(fill="x", pady=10)

    ttk.Button(profile_window, text="Change Password", command=change_password).pack(pady=5)
    ttk.Button(profile_window, text="Edit Addresses", command=edit_addresses).pack(pady=5)
    ttk.Button(profile_window, text="Edit Payment Methods", command=edit_payment_methods).pack(pady=5)

def change_password():
    # Implement password change functionality
    print("Change Password")

def edit_addresses():
    # Implement address editing functionality
    print("Edit Addresses")

def edit_payment_methods():
    # Implement payment method editing functionality
    print("Edit Payment Methods")

root = tk.Tk()
root.title("Shopping App")

# Button to open profile page
ttk.Button(root, text="My Profile", command=open_profile_page).pack(pady=20)

root.mainloop()
