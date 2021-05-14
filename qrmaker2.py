from tkinter import *
import threading
from tkinter import messagebox,filedialog
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import ttk
root = Tk()
root.geometry("200x220")
root.title('PyQR')
root.resizable(False, False)
#root.resizable(False, False)
name1 = Label(root, text = "PyQR",font=('Arial', 14)).place(x = 75,y = 10)
name1 = Label(root, text = "Enter text",font=('Arial', 10)).place(x = 70,y = 40)
files = [('Portable Network Graphics',"*.png"),('All Files', '*.*')]

def captn(url):
    file = filedialog.asksaveasfile(filetypes = files, defaultextension = ".png")
    file=str(file)
    b=file.split()
    c=b[1]
    d=c.split("=")
    file=d[1][1:-1]
    #print(file)
    url2 = pyqrcode.create(url)
    url2.png(file, scale = 12)
    messagebox.showinfo("PyQR","QR code generated")
    

def on_change(e1):
    global url
    try:
        url=e1.widget.get()
    except:
        url=e1.get()
    #print(url)
    if url=="":
        messagebox.showerror("PyQR","Enter text")
    else:
        t2 = threading.Thread(target=captn, args=(url,))
        t2.start()

e1 = Entry(root,width=25)
e1.place(x=20,y=80)
e1.bind("<Return>", on_change)
ext17=ttk.Button(root,text="Make QR code",command=lambda: on_change(e1))
ext17.place(x=60,y=130)

root.mainloop()
