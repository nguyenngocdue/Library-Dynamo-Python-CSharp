import tkinter as tk
from tkinter import messagebox

def submit_action():
    user_info = f"Name: {entry_name.get()}\nEmail: {entry_email.get()}\nMessage: {text_message.get('1.0', tk.END)}"
    messagebox.showinfo("Form Submitted", user_info)

# Create the main window
root = tk.Tk()
root.title("Simple Form")

# Create a label for the name
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, sticky="w")

# Create an entry for the name
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

# Create a label for the email
label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, sticky="w")

# Create an entry for the email
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

# Create a label for the message
label_message = tk.Label(root, text="Message:")
label_message.grid(row=2, column=0, sticky="nw")

# Create a text field for the message
text_message = tk.Text(root, height=5, width=25)
text_message.grid(row=2, column=1)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=3, column=1, sticky="e")

# Run the application
root.mainloop()
