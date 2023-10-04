from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
#------------------------Password Generator-----------------------#

#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for char in range(randint(8,10))]

    password_symbols=[choice(symbols) for char in range(randint(2,4))]

    password_numbers=[choice(numbers) for char in range(randint(2,4))]

    password_list = password_letters+ password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.insert(0, password)

    pyperclip.copy(password)





#------------------------Save Password----------------------------#

def save_data():

    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd

         }
    }

    if website != "" and email != "" and pwd != "":

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                                                              f"\nPassword: {pwd} \nIs it okay to save? "
                                       )

        if is_ok:
            try:
                with open("data.json", "r") as data_file:

                    try:
                        data = json.load(data_file)
                    except ValueError:
                        raise FileNotFoundError

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)


    else:
        messagebox.showerror(title="Empty Fields", message="Please fill all the empty fields.")


#-------------------------Website Search---------------------------#

def search():

    website = website_entry.get()

    try:
        with open('data.json', 'r') as data_file:
            try:
                data = json.load(data_file)
            except ValueError:
                messagebox.showerror(title="Empty File", message="Please add some data")


    except FileNotFoundError:
        messagebox.showerror(title="File Error", message="Please add some data")
    else:
        if website in data:
            email = data[website]['email']
            pwd = data[website]['password']

            messagebox.showinfo(title="Search Result", message=f"Email:{email}\n"
                                                       f"Password:{pwd}")
        else:
            messagebox.showerror(title="Not Found", message=f"No details for {website}")



#-------------------------UI Setup---------------------------------#

window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)



canvas = Canvas(window, width=200, height=200)
imgobj = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=imgobj)
canvas.grid(column=1,row=0)

website_label = Label(text='Website:')
website_label.grid(column = 0, row = 1)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column = 1, row = 1)

email_label = Label(text='Email/Username:')
email_label.grid(column = 0, row = 2)

email_entry = Entry(width=35)
email_entry.insert(0, 'dummy@mail.com')
email_entry.grid(column = 1, row = 2, columnspan = 2)

pwd_label = Label(text='Password:')
pwd_label.grid(column = 0, row = 3)

pwd_entry = Entry(width=21)
pwd_entry.grid(column = 1, row = 3)



btn_generate = Button(text='Generate Password', command=generate_password)
btn_generate.grid(column=2, row=3)

btn_add = Button(text='Add', width=36, bg='light blue', fg='black', command=save_data)
btn_add.grid(column=1, row=4, columnspan = 2)

btn_search = Button(text="Search", width=13, command=search)
btn_search.grid(column=2, row=1)






window.mainloop()
