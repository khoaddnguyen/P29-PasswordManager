from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = pw_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askyesno(title=website, message=f"Is it ok to save?"
                                                   f"\nEmail: {email} "
                                                   f"\n Password: {password}")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                pw_entry.delete(0, END)
        # else: do nothing when click "Cancel" on pop up


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
email_entry.insert(END, "123@gmail.com")  # display an email string when open program

pw_entry = Entry(width=20)
pw_entry.insert(END, string="")
pw_entry.grid(column=1, row=3)

# Buttons

generate_pw_button = Button(text="Generate Password",width=11)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()