from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\acer\Desktop\Investhub\build\assets\frame0")
DATABASE_PATH = OUTPUT_PATH / "investhub.db"

def create_database():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (group_id INTEGER, user_id INTEGER, user_name TEXT)''')
    conn.commit()
    conn.close()

def open_new_window():
    new_window = Toplevel(window)
    new_window.geometry("1368x762")
    new_window.title("New Page")

    canvas = Canvas(
        new_window,
        bg="#FFFFFF",
        height=767,
        width=1367,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    background_image = PhotoImage(file=relative_to_assets(r"C:\Users\acer\Desktop\shopping cart\build\assets\frame0\image_1.png"))
    canvas.create_image(683.0, 383.0, image=background_image)

    # Rectangle 1
    canvas.create_rectangle(-3.0, 351.0, 1367.0, 354.0, fill="#000000", outline="")

    # Rectangle 2
    canvas.create_rectangle(-3.0, 426.0, 1358.0, 429.0, fill="#000000", outline="")

    # Rectangle 3
    canvas.create_rectangle(-3.0, 501.0, 1358.0, 504.0, fill="#000000", outline="")

    # Rectangle 4
    canvas.create_rectangle(-3.0, 576.0, 1358.0, 579.0, fill="#000000", outline="")

    # Rectangle 5
    canvas.create_rectangle(-3.0, 651.0, 1358.0, 654.0, fill="#000000", outline="")
    button_image_1 = PhotoImage(
    file=relative_to_assets("button.png"))
    button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
    button_1.place(
    x=749.0,
    y=38.0,
    width=542.0,
    height=109.0
)
    
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()

    for row in data:
        group_id_label = Label(new_window, text=f"Group ID: {row[0]}")
        group_id_label.pack()
        user_id_label = Label(new_window, text=f"User ID: {row[1]}")
        user_id_label.pack()
        user_name_label = Label(new_window, text=f"User Name: {row[2]}")
        user_name_label.pack()

    new_window = Toplevel(window)
    new_window.geometry("1368x762")
    new_window.title("New Page")

    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    
    for row in data:
        group_id_label = Label(new_window, text=f"Group ID: {row[0]}")
        group_id_label.pack()
        user_id_label = Label(new_window, text=f"User ID: {row[1]}")
        user_id_label.pack()
        user_name_label = Label(new_window, text=f"User Name: {row[2]}")
        user_name_label.pack()

def save_data(group_id, user_id, user_name):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO users (group_id, user_id, user_name) VALUES (?, ?, ?)", (group_id, user_id, user_name))
    conn.commit()
    conn.close()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

create_database()

window = Tk()
window.geometry("1366x768")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 12.0, 1366.0, 780.0, fill="#FFFFFF", outline="")
background_image = PhotoImage(file=relative_to_assets(r"c:\Users\acer\Downloads\grpshoppingedited (1).png"))
canvas.create_image(0, 0, anchor='nw', image=background_image)

canvas.create_text(
    740.0,
    332.0,
    anchor="nw",
    text="GROUP ID",
    fill="#000000",
    font=("Poppins Regular", 36 * -1)
)

canvas.create_text(
    740.0,
    417.0,
    anchor="nw",
    text="USER ID",
    fill="#000000",
    font=("Poppins Regular", 36 * -1)
)

canvas.create_text(
    740.0,
    502.0,
    anchor="nw",
    text="USER NAME",
    fill="#000000",
    font=("Poppins Regular", 36 * -1)
)

group_id_entry = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 18)
)
group_id_entry.place(
    x=991.5,
    y=339.0,
    width=262.0,
    height=47.0
)

user_id_entry = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 18)
)
user_id_entry.place(
    x=991.5,
    y=417.0,
    width=262.0,
    height=47.0
)

user_name_entry = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Regular", 18)
)
user_name_entry.place(
    x=991.5,
    y=510.0,
    width=262.0,
    height=47.0
)

def save_and_open():
    
    group_id = group_id_entry.get()
    user_id = user_id_entry.get()
    user_name = user_name_entry.get()
    
    save_data(group_id, user_id, user_name)
    open_new_window()

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=save_and_open,
    relief="flat"
)
button_1.place(
    x=895.0,
    y=602.0,
    width=302.0,
    height=81.0
)

window.resizable(False, False)
window.mainloop()
