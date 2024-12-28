from tkinter import *
import webbrowser
from random import choice
import string

def gen_password():
    password_lenght = int(password_l.get())
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(password_lenght))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#make the window
window = Tk()
window.title("Password Generator - free , open_source")
window.geometry("1440x960")
window.iconbitmap("diamond.ico")
window.config(background="#3c2487")

#make principal frame
frame = Frame(window, bg="#3c2487")

#make image
width = 600
height = 700
image = PhotoImage(file="password.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#3c2487", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous_boite
right_frame = Frame(frame, bg="#3c2487", )

#make title
label_title = Label(right_frame, text="Password Generator", font=("The Wild Breath of Zelda", 50), bg="#3c2487", fg="white")
label_title.pack()

#make champ
password_entry = Entry(right_frame, font=("Helvetica", 40), bg="#3c2487", fg="white")
password_entry.pack()

#make button
gen_button = Button(right_frame, text="Generate", font=("Helvetica", 30), bg="#c8c3d6", fg="#3c2487", command=gen_password)
gen_button.pack(pady=25)

#make inttitle
int_title = Label(right_frame, text="Number of characters", font=("Helvetica", 30), bg="#3c2487", fg="white")
int_title.pack()

#make champ2
password_l = Entry(right_frame, font=("Helvetica", 40), bg="#3c2487", fg="white")
password_l.pack()

#place subframe
right_frame.grid(row=0, column=1, sticky=W)

#afficher frame
frame.pack(expand=YES)

# create barre de menu
menu_bar = Menu(window)
# make menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="quit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

#afficher window
window.mainloop()
