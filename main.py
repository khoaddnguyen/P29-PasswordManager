from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png")  # file directory
canvas = Canvas(width=200, height=200, highlightthickness=0)  # pixels are even numbers only
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


# Labels

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

pw_label = Label(text="Password: ")
pw_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(END, string="")
email_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=20)
pw_entry.insert(END, string="")
pw_entry.grid(column=1, row=3)

# Buttons

generate_pw_button = Button(text="Generate Password",width=11)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()