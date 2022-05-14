import datetime
import urllib.request
from lxml import html
import tkinter as tk

root = tk.Tk()
root.title("比特币实时价格");
root.geometry("500x140");
root.config(bg="black");

frame = tk.Frame(root,bg="black");
frame.pack(pady=20);

logo = tk.PhotoImage(file="./bitcoin.png");
canvas = tk.Canvas(frame,bg="black",width=100,height=100,highlightthickness=0)
canvas.grid(row=0,column=0,rowspan=2)
canvas.create_image(50,50,image=logo)

price_lable = tk.Label(frame,text="Price",font=("Ds-Digital",45),bg="black",fg="cyan",bd=0);
price_lable.grid(row=0,column=1,padx=20,sticky=tk.S);

dateTime_label = tk.Label(frame,text="datetime",font=("Ds-Digital",12),bg="black",fg="cyan",bd=0);
dateTime_label.grid(row=1,column=1,sticky=tk.N);

root.mainloop();