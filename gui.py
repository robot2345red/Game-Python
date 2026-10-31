import customtkinter as ctk
from main import guess
root = ctk.CTk()
root.resizable(False,False)

label = ctk.CTkLabel(root,text='Guess between 1 & 1000')
entry = ctk.CTkEntry(root)
button = ctk.CTkButton(root,text='Check',command=guess)
reward = ctk.CTkLabel(root,text='')

label.pack()
entry.pack()
button.pack()
reward.pack()
