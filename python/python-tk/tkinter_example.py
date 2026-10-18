from tkinter import *

root = Tk()


root.title("Test Application")
root.geometry("600x400")

label_one = Label(root, text="Enter Your Username")
label_one.grid(row=0)

text_one = Entry(root, width=80)
text_one.grid(row=1)

label_two = Label(root, text="Enter Your Password")
label_two.grid(row=2)

text_two = Entry(root, width=80, text="ll")
text_two.grid(row=3)

button_one = None

def create_new_layout():
    label_three = Label(root, text="Welcome")
    label_three.grid(row=0)

def check_login():
    if text_one.get() == "user123" and text_two.get() == "123":
        label_one.destroy()
        label_two.destroy()
        button_one.destroy()
        text_one.destroy()
        text_two.destroy()
        create_new_layout()
    else:
        label_two.configure(text="Incorrect Password, Enter Correct Password") 
    

button_one = Button(root, width=80, text="Login", command=check_login)
button_one.grid(row=4)

root.mainloop()