import urllib.request
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__();
        self.title("ip");
        self.geometry("300x100");
        
        ip = urllib.request.urlopen("http://api.ipify.org").read().decode();
        self.label_ip = tk.Label(self,text=ip,font=("微软雅黑",20));
        self.label_ip.pack(expand=True);
        
if __name__ == "__main__":
    app = Application();
    app.mainloop();
    