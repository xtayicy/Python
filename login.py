import tkinter as tk
from PIL import Image,ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__();
        self.title("登陆");
        self.geometry("300x150");
        
        self.init_widgets();
        
    def init_widgets(self):
        self.frame = tk.Frame(self);
        
        self.label_username = tk.Label(self.frame,text="username",anchor=tk.W);
        self.label_username.pack(fill=tk.X);
        
        self.text_username = tk.Entry(self.frame);
        self.text_username.pack(fill=tk.X);
        
        self.label_password = tk.Label(self.frame,text="password",anchor=tk.W);
        self.label_password.pack(fill=tk.X);
        
        self.text_password = tk.Entry(self.frame,show="*");
        self.text_password.pack(fill=tk.X);
        
        self.button_login = tk.Button(self.frame,text="login",width=16);
        self.button_login.pack(side=tk.LEFT,pady=10);
        
        self.button_cancel = tk.Button(self.frame,text="cancel",width=16,command=lambda:self.destroy());
        self.button_cancel.pack(side=tk.RIGHT,pady=10);
        
        self.frame.pack(padx=20,pady=5,fill=tk.X);
        
if __name__ == "__main__":
    app = Application();
    app.mainloop();