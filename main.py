from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

# List Comprehension: new_list = [new_item for item in list]
password_letters = [random.choice(letters) for _ in range(0, nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(0, nr_symbols)]
password_numbers = [random.choice(numbers) for _ in range(0, nr_numbers)]

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
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