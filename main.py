from tkinter import *
from tkinter import messagebox
import random
import json
#------------------------Password Generator-----------------------#




#------------------------Save Password----------------------------#

def save_data():

    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()

    print(website)




    if website != "" and email != "" and pwd != "":

        print('heee')

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                                                              f"\nPassword: {pwd} \nIs it okay to save? "
                                       )

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {pwd}\n")
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)

    else:
        messagebox.showerror(title="Empty Fields", message="Please fill all the empty fields.")








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

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column = 1, row = 1, columnspan = 2)

email_label = Label(text='Email/Username:')
email_label.grid(column = 0, row = 2)

email_entry = Entry(width=35)
email_entry.insert(0, 'dummy@mail.com')
email_entry.grid(column = 1, row = 2, columnspan = 2)

pwd_label = Label(text='Password:')
pwd_label.grid(column = 0, row = 3)

pwd_entry = Entry(width=21)
pwd_entry.grid(column = 1, row = 3)



btn_generate = Button(text='Generate Password')
btn_generate.grid(column=2, row=3)

btn_add = Button(text='Add', width=36, bg='light blue', fg='black', command=save_data)
btn_add.grid(column=1, row=4, columnspan = 2)






window.mainloop()
