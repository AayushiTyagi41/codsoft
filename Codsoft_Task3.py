import random, string
from tkinter import *
import pyperclip

root =Tk()
root.geometry("420x420") 
root.title("Random Password Generator")

output_pass = StringVar()

all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  

def randPassGen():
    password = "" 
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   
        password = password + random.choice(char_type)
    
    output_pass.set(password)

def copyPass():
    pyperclip.copy(output_pass.get())


pass_head = Label(root, text = 'Password Length', font = 'arial 13 bold').pack(pady=10)
pass_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='arial 17').pack()


Button(root, command = randPassGen, text = "Generate Password", font="Arial 11", bg='skyblue', fg='brown', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

pass_label = Label(root, text = 'Random Generated Password', font = 'arial 13 bold').pack(pady="32 13")
Entry(root , textvariable = output_pass, width = 25, font='arial 17').pack()


Button(root, text = 'Copy to Clipboard', command = copyPass, font="Arial 10", bg='orange', fg='white', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

root.mainloop()  
