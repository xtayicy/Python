import tkinter as tk
import time

class Clock(tk.Tk):
    def __init__(self):
        super().__init__();
        
        self.title("时钟");
        
        self.time_text = "";
        self.label_time = tk.Label(self,text=self.time_text,font=("ds-digital",80),padx=10,pady=10,background="black",foreground="cyan");
        self.label_time.pack();
        self.update_time();
        
    def update_time(self):
        self.time_text = time.strftime("%y-%m-%d\n%H:%M:%S %p");
        self.label_time.config(text=self.time_text);
        self.after(1000, self.update_time);
        
if __name__ == "__main__":
    app = Clock();
    app.mainloop();        