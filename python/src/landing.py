"""Landing Page.

Mockup Landing Page
"""
import tkinter as tk
from os import getcwd
from os.path import join, isfile

def landing():
    root = tk.Tk()
    root.geometry("800x480")
    root.wm_attributes('-fullscreen', 'true')
    tk.Label(master=root,
             text="Loyalty", font=("courier", 48))\
        .grid(row=0, column=0, columnspan=3)
    phone = tk.PhotoImage(file=join(getcwd(), "media", "phone.gif"))
    app = tk.PhotoImage(file=join(getcwd(), "media", "app.gif"))
    email = tk.PhotoImage(file=join(getcwd(), "media", "email.gif"))

    root.columnconfigure(0, minsize=310)
    root.columnconfigure(1, minsize=180)
    root.columnconfigure(2, minsize=310)
    root.rowconfigure(0, minsize=180)

    tk.Button(master=root, image=phone,
              relief="flat")\
        .grid(row=1, column=0, sticky="e")
    tk.Button(master=root, image=app,
              relief="flat")\
        .grid(row=1, column=1)
    tk.Button(master=root, image=email,
              relief="flat")\
        .grid(row=1, column=2, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    landing()