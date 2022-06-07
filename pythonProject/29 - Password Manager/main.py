from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # generate random lists
    random_letters = random.sample(letters, nr_letters)
    random_symbols = random.sample(symbols, nr_symbols)
    random_numbers = random.sample(numbers, nr_numbers)

    # combine lists
    total = random_letters + random_symbols + random_numbers

    # randomize the combined list
    random_password_list = random.sample(total, len(total))

    # Transform list to string
    # You can add a space between '' for a space between each letter
    listToStr = ''.join(map(str, random_password_list))
    print(listToStr)
    password_input.delete(0, "end")
    password_input.insert(0, listToStr)
    pyperclip.copy(listToStr)

    # Option 2 to tranform list to string

    # password = ""
    # for char in random_password_list:
    #   password += char

    # print(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Error", message="You didn't fill in all fields.")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n "
                                                              f"Website: {website} \n "
                                                              f""f"Username: {username} \n "
                                                              f"Password: {password} \n "
                                                              f"Is it ok?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"Website: {website} | Email/Username: {username} | Password: {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website -----------------------------------------------------------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(padx=2, pady=2)

website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")


# email / username --------------------------------------------------
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_label.config(padx=2, pady=2)

username_input = Entry(width=36)
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, "email@email.com")

# password --------------------------------------------------
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=2, pady=2)

password_input = Entry(width=24)
password_input.grid(column=1, row=3, sticky="W")

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

# add to file --------------------------------------------------
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")







window.mainloop()