import requests
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Chuck Norris curious facts')

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

def fact():

    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "7160ab3875mshdb37df9341ab8abp15938bjsn055e56aeb1c5",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    json = response.json()

    value = json['value']
   
    messagebox.showinfo('Interest fact:','{}'.format(value))

frame1 = tk.Frame(master = window, width = 300, height = 300, bg = "light yellow")
frame1.pack(fill = tk.BOTH , expand = True)

label1 = tk.Label( master = frame1,text = "Click button to get curious fact about Chuck Norris",bg = "light yellow")
label1.grid(row = 0,column = 2,padx = 10,pady = 10,sticky = "sn")

button1 = tk.Button( master = frame1 ,text = "Click me to show fact",command = fact)
button1.grid(row = 4,column = 2,padx = 10,pady = 10)

window.mainloop()
