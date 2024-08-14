import tkinter as tk
from Calendar import Calendar
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Albert Calendar")
root.geometry("300x300")
root.configure(bg="lightblue")

# Create login labels and entries
username_label = tk.Label(root, text="Username", borderwidth=0, relief="flat", bg="lightblue")
username_entry = tk.Entry(root, borderwidth=0, relief="flat")
password_label = tk.Label(root, text="Password", borderwidth=0, relief="flat", bg="lightblue")
password_entry = tk.Entry(root, borderwidth=0, relief="flat")

# Place the labels and entries on a grid
username_label.grid(row=1, column=0, pady=40, padx=20)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0, pady=0, padx=20)
password_entry.grid(row=2, column=1)

# Function to handle login
def Login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        # Show an error message if any field is empty
        messagebox.showerror("Input Error", "Both username and password are required!")
    else:
        # Proceed with the calendar if login is successful
        root.destroy()
        Calendar()

# Create and place the login button
button = tk.Button(root, text="Login", command=Login)
button.grid(row=3, column=1, pady=10)

# Run the application
root.mainloop()