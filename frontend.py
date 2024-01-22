import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import urllib.request, json, datetime, random, string, os

#tkinter main
root = Tk()
root.geometry("500x350")
root.resizable(0, 0)
root.title('Warp+')
root.iconbitmap(r'C:\Users\saeed\PycharmProjects\pythonProject\.venv\mymoudle\icon.ico')

# values
ti = 1
xi = ti * 10
b = 0
g = 0
referrer = "test"
running = False
log = ""
v1 = StringVar(root)

# labels & entry & btns
l0 = tk.Label(root, text="WARP PLUS CLOUDFLARE By Zoomlord", font=("Roboto Light", 10, "bold"))
l0.place(x=120, y=30)
l1 = tk.Label(root, text="Enter Your Device ID:", font=("Roboto Light", 9, "bold")).place(x=10, y=80)
l2 = tk.Label(root, text="Good:", font=("Roboto Light", 9, "bold")).place(x=180, y=120)
l21 = tk.Label(root, text=g, font=("Roboto Light", 9, "bold"), fg="green")
l21.place(x=215, y=120)
l3 = tk.Label(root, text="Bad:", font=("Roboto Light", 9, "bold")).place(x=250, y=120)
l31 = tk.Label(root, text=b, font=("Roboto Light", 9, "bold"), fg="red")
l31.place(x=280, y=120)
l5 = Label(root, text=log)
l5.place(x=140, y=175)
ent1 = ttk.Entry(root, textvariable=v1, width=35)
ent1.place(x=135, y=80)

s = ttk.Style()
s.configure('my.TButton',font=('Roboto Light', 9, "bold"))
btn2 = ttk.Button(root, text="submit",style='my.TButton', command=lambda: subm())
btn2.place(x=370, y=77, width=100)

progressbar = ttk.Progressbar()
progressbar.place(x=50, y=200, width=400)

stop = ttk.Button(root, text="Stop",style='my.TButton', command=lambda: on_stop(),state=tk.DISABLED)
stop.place(x=290, y=260, width=70)
start = ttk.Button(root, text="Start",style='my.TButton', command=lambda: on_start(),state=tk.DISABLED)
start.place(x=150, y=260, width=70)

btn3 = ttk.Button(root, text="-",style='my.TButton', command=lambda : counter(0))
btn3.place(x=220, y=260, width=20)
btn4 = ttk.Button(root, text="+",style='my.TButton', command=lambda : counter(1))
btn4.place(x=270, y=260, width=20)
l6 = ttk.Label(root, text=ti, font=("Roboto Light", 9, "bold"))
l6.place(x=246, y=263)
# menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Tutorial", font=("Roboto Light", 9),command=lambda: NewRoot())
filemenu.add_command(label="Version", font=("Roboto Light", 9),command=lambda: messagebox.showinfo("Info", "Version : 1.0.0"))
filemenu.add_separator()
filemenu.add_command(label="Exit", font=("Roboto Light", 9), command=root.quit)
menubar.add_cascade(label="Help", font=("Roboto Light", 9), menu=filemenu)
root.config(menu=menubar)

#binds
def undotext(txt):
    ent1.delete(0, 'end')
def popup(event):
    try:
        menu.tk_popup(event.x_root,event.y_root)
    finally:
        menu.grab_release()
def paste():
    clipboard = root.clipboard_get()
    ent1.insert('end',clipboard)
def copy():
    inp = ent1.get()
    root.clipboard_clear()
    root.clipboard_append(inp)

menu = Menu(root,tearoff=0)
menu.add_command(label='Copy',command=copy)
menu.add_command(label='Paste',command=paste)
ent1.bind('<Button-3>',popup)
ent1.bind("<Control-v>")
ent1.bind("<Control-z>", undotext)

#functions
def NewRoot():
    NewRoot = Toplevel(root)
    NewRoot.title("Tutorial")
    NewRoot.geometry("500x350")
    NewRoot.resizable(0, 0)
    NewRoot.iconbitmap("icon.ico")
    T = Text(NewRoot, height=15, width=54, font=("Roboto Light", 12))
    l = Label(NewRoot, text="How to do it?")
    l.config(font=("Roboto Regular", 14))
    text = """1- Open the software, at the right bottom you can see the setting icon\n2- click on it and select preferences\n3- in current tab (General) you can see the Device ID\n4- copy that and paste it in this software\n5- you can increase the duration and click on start\n6- Enjoy your free WARP+!!"""
    btn = ttk.Button(NewRoot, text="Exit",width=10, command=NewRoot.destroy)
    l.pack()
    T.pack()
    btn.pack()
    T.insert(tk.END, text)

def subm():
    data = ent1.get()

    if len(data) < 35 :#or len(data) > 36:
        messagebox.showerror("Your ID is Wrong", "Please enter the Correct ID")
        ent1.delete(0, 'end')
    else:
        btn2.state(["disabled"])
        start.config(state=NORMAL)
        global referrer
        referrer = data
def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(stringLength))
    except Exception as error:
        print(error)

def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join(random.choice(digit) for _ in range(stringLength))
    except Exception as error:
        print(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
    try:
        install_id = genString(22)
        body = {
            "key": f"{genString(43)}=",
            "install_id": install_id,
            "fcm_token": f"{install_id}:APA91b{genString(134)}",
            "referrer": referrer,
            "warp_enabled": False,
            "tos": f"{datetime.datetime.now().isoformat()[:-3]}+02:00",
            "type": "Android",
            "locale": "es_ES",
        }
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        return response.getcode()
    except Exception as error:
        l7 = Label(root, text=error, fg="red")
        l7.place(x=140, y=225)


def progressBar():
    for i in range(100):
        if progressbar["value"] == 100:
            progressbar.stop()
            updatetext(1,"Request completed...")
            showgig()
            break
        else:
            progressbar["value"] += 1
            progressbar.update_idletasks()
            updatetext(1,f"Waiting response...")
            root.after(100, progressBar)
            break

def on_start():
    if ti > 0:
        my_mainloop()
        start.config(state=DISABLED)
        stop.config(state=NORMAL)
        btn3.config(state=DISABLED)
        btn4.config(state=DISABLED)
    else:
        updatetext(1, "Program can not start with 0 duration!!")

def on_stop():
    start.config(state=NORMAL)
    stop.config(state=DISABLED)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    start.tkraise()
    global ti
    ti = 0
    updatetext(1, "Program Stoped!!")

def counter(td):
    global ti
    if td == 1:
       ti += 1
       l6.config(text=ti)
    else:
        if ti > 0:
           ti -= 1
           l6.config(text=ti)

def updatetext(var, tx):
    if var == 1:
        l5.config(text="")
        l5.config(text=tx)
    elif var == 2:
        l31.config(text=tx)
    elif var == 3:
        l21.config(text=tx)
    elif var == 4:
        l6.config(text=tx)

def showgig():
    l4 = Label(root, text="GB has been successfully added to your account.", fg="green")
    l4.place(x=160, y=150)
    l41 = Label(root, text=g)
    l41.place(x=120, y=150)

def my_mainloop():
    global b,g,ti,xi
    result = run()
    if ti == 0:
        start.config(state=NORMAL)
        stop.config(state=DISABLED)
        btn3.config(state=NORMAL)
        btn4.config(state=NORMAL)
        updatetext(1, "")
    if ti > 0:
        if result == 200:
            updatetext(1, "Sending request...")
            g += 1
            xi -= 1
            updatetext(4,ti)
            updatetext(3,g)
            updatetext(1,f"WORKING ON ID: {referrer}")
            progressBar()
            if ti > 1:
                updatetext(1,f"After {xi} seconds, a new request will be sent.")
            ti -= 1
            final_time = (xi * 1000)
            root.after(final_time, my_mainloop)
        else:
            updatetext(1, "Sending request...")
            b += 1
            xi -= 1
            updatetext(4, ti)
            updatetext(2,b)
            updatetext(1,"Error when connecting to server.")
            if ti > 1:
                updatetext(1,f"After {xi} seconds, a new request will be sent.")
            ti -= 1
            final_time = (xi * 1000)
            root.after(final_time, my_mainloop)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root.mainloop()
