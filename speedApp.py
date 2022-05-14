import threading
import tkinter as tk
from tkinter import ttk
import speedtest

root = tk.Tk()
root.geometry("400x200")
root.title("网速测试")

frm = tk.LabelFrame(root, text="测试结果")
frm.pack(padx=10, pady=10, fill=tk.X)

lbl_d = tk.Label(frm, text="DOWNLOAD:", font=("DS-Digital", 20))
lbl_d.grid(row=0, column=0, sticky=tk.W, padx=10)

lbl_dr = tk.Label(frm, text="", font=("DS-Digital", 20))
lbl_dr.grid(row=0, column=1, sticky=tk.W, padx=10)


lbl_u = tk.Label(frm, text="UPLOAD:", font=("DS-Digital", 20))
lbl_u.grid(row=1, column=0, sticky=tk.W, padx=10)

lbl_ur = tk.Label(frm, text="", font=("DS-Digital", 20))
lbl_ur.grid(row=1, column=1, sticky=tk.W, padx=10)


def start_test():
    def action():
        t = speedtest.Speedtest()
        pb.pack(padx=10, pady=10)
        pb.start()
        t.get_servers()
        dr = t.download()
        ur = t.upload()
        lbl_dr.config(text=dr / 1024 / 1024)
        lbl_ur.config(text=ur / 1024 / 1024)
        pb.stop()
        pb.pack_forget()
        btn.config(state=tk.NORMAL)
    btn.config(state=tk.DISABLED)
    threading.Thread(target=action).start()


pb = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=380, mode="indeterminate")

btn = tk.Button(root, text="开始测速", height=2, command=start_test)
btn.pack(padx=10, pady=5, fill=tk.X, expand=True)


root.mainloop()
