import re
import tkinter as tk


def validate_email():
    email = entry_email.get()

    if "@" not in email:
        result = "Invalid Email. Missing '@'!"
        color = "red"
    elif "." not in email:
        result = "Invalid Email. Missing '.'!"
        color = "red"
    else:
        pattern = r"^[A-Za-z][A-Za-z0-9_-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$"
        if re.match(pattern, email):
            result = "Email is valid!"
            color = "green"
        else:
            result = "Invalid email!"
            color = "red"

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)
    entry_result.config(fg=color)



root = tk.Tk()
root.geometry("500x500")
root.title("Email Validator")

label_instructions = tk.Label(root, text="Enter an email address. It should include '@' and '.domain'!")
label_instructions.pack()

entry_email = tk.Entry(root, width=60)
entry_email.pack()
entry_email.delete(0, tk.END)

button_validate = tk.Button(root, text="Validate Email", command=validate_email)
button_validate.pack()

entry_result = tk.Entry(root, width=60)
entry_result.pack()
entry_result.delete(0, tk.END)

root.mainloop()
