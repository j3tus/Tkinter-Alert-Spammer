from tkinter import *
from tkinter import messagebox
from time import sleep
from colorama import Fore
import random
import decimal
import sys
from PIL import ImageTk, Image


App = Tk() 
App.withdraw()
App.iconbitmap(default='blank.ico')
lab = Label(App, text='transparent icon')
lab.pack()

alertapp = Toplevel (App)
alertapp.attributes ('-topmost', True)
alertapp.mainloop
alertapp.withdraw()

im = Image.open("cross.png")
ph = ImageTk.PhotoImage(im)
img = Label(App, image=ph)
img.place(x=100, y=100)

print(f"{Fore.CYAN} Starting alerts.. {Fore.RESET}")
sleep(0.3)
count = 0
for i in range(25):
    print(f"{Fore.BLUE} Opened error message {Fore.YELLOW} {count} {Fore.RESET}")
    messagebox.showerror(title="Windows Update Standalone Installer", message="Windows Update Standalone Installer!\n\n Cannot find C:\Windows\System32: ")
    print(f"{Fore.BLUE}> Closed error message {Fore.RESET}")
    time= decimal.Decimal(random.randrange(0, 40))/10
    print(f"\n{Fore.WHITE} INFO: Next alert {time}s {Fore.RESET}")
    sleep(int(time))
    count = count + 1
print(f"\n{Fore.GREEN} User closed all messages ({count}) {Fore.RESET}")
sleep(0.5)
print(f"{Fore.RED} Closing..{Fore.RESET}")
sys.exit()

