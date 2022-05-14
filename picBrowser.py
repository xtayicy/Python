import tkinter as tk
from PIL import ImageTk
from click.core import Command

root = tk.Tk();
root.title("图片浏览器");

images = [
    ImageTk.PhotoImage(file="images/001.jpg"),
    ImageTk.PhotoImage(file="images/002.jpg"),
    ImageTk.PhotoImage(file="images/003.jpg"),
    ImageTk.PhotoImage(file="images/004.jpg"),
    ImageTk.PhotoImage(file="images/005.jpg")
]

current = 0;

def shift_image(direction:str) -> None:
    global current
    if direction == "prev":
        current -= 1;
    
    if direction == "next":
        current += 1;
    
    display_image(current);

def display_image(index:int) -> None:
    global label_img
    label_img['image'] = images[index];
    
    button_prev['state'] = tk.DISABLED if index <=0 else tk.NORMAL;
    button_next['state'] = tk.DISABLED if index >= len(images) - 1 else tk.NORMAL;

label_img = tk.Label(image=images[current]);
label_img.grid(row=0,column=0,columnspan=3);

button_prev = tk.Button(root,text="<<<",pady=10,command=lambda:shift_image("prev"));
button_prev.grid(row=1,column=0,sticky=tk.W+tk.E);
button_exit = tk.Button(root,text="Exit",pady=10,command=root.quit);
button_exit.grid(row=1,column=1,sticky=tk.W+tk.E);
button_next = tk.Button(root,text=">>>",pady=10,command=lambda:shift_image("next"));
button_next.grid(row=1,column=2,sticky=tk.W+tk.E);

display_image(current);

root.mainloop();
