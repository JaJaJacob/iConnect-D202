import time
import datetime
import subprocess
import pynput.mouse
import requests
from tkinter import *
import psutil

# check resulution
main_window = Tk()
width = main_window.winfo_screenwidth()
height = main_window.winfo_screenheight()
widthC = float(width / height)

# functions
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def main_functionality():
    mouse = pynput.mouse.Controller()
    if widthC > 1.76 and widthC < 1.79:
        widthb = int(width / 2.04)
        heightD = int(207)
        mouse.position = (widthb, heightD)
        time.sleep(13)
        mouse.press(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.left)

    if widthC > 1.55 and widthC < 1.7:
        widthb = int(width / 1.73)
        heightD = int(207)
        mouse.position = (widthb, heightD)
        time.sleep(13)
        mouse.press(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.left)


def mainFuncionalityFast():
    mouse = pynput.mouse.Controller()
    if widthC > 1.76 and widthC < 1.79:
        widthb = int(width / 2.04)
        heightD = int(207)
        mouse.position = (widthb, heightD)
        time.sleep(5)
        mouse.press(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.left)

    if widthC > 1.55 and widthC < 1.7:
        widthb = int(width / 1.73)
        heightD = int(207)
        mouse.position = (widthb, heightD)
        time.sleep(5)
        mouse.press(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.left)


def close_functionality():
    mouse = pynput.mouse.Controller()
    mouse.position = (width, 0)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)


def rudak_command():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/3TMVWLQP"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call("start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/3TMVWLQP", shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call("start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/3TMVWLQP",shell=True)
            main_functionality()
            close_functionality()

def drazba_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/3TMVWLQP"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call("start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/4BQ1KUCV", shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call("start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/4BQ1KUCV",shell=True)
            main_functionality()
            close_functionality()


def chaladyniak_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/3C8E8GO2"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/3C8E8GO2",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/3C8E8GO2",
                shell=True)
            main_functionality()
            close_functionality()


def winnicki_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/WPD2P00X"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/WPD2P00X",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/WPD2P00X",
                shell=True)
            main_functionality()
            close_functionality()


def lewicki_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/CAG7DLVO"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/CAG7DLVO",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/CAG7DLVO",
                shell=True)
            main_functionality()
            close_functionality()


def kopcial_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/3Q7MLQ0I"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/3Q7MLQ0I",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/3Q7MLQ0I",
                shell=True)
            main_functionality()
            close_functionality()


def szewczyk_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/NU44F60N"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/NU44F60N",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/NU44F60N",
                shell=True)
            main_functionality()
            close_functionality()


def zaikin_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/92MKP4JP"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/92MKP4JP",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/92MKP4JP",
                shell=True)
            main_functionality()
            close_functionality()


def figielska_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/6HOBVLF2"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/6HOBVLF2",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/6HOBVLF2",
                shell=True)
            main_functionality()
            close_functionality()


def gniazdowski_commmand():
    url = "https://meet.lync.com/wwsiedupl/wwsi365/O0GEDZCD"
    page = requests.get(url)
    print(page.status_code)
    if checkIfProcessRunning('chrome'):
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/O0GEDZCD",
                shell=True)
            mainFuncionalityFast()
            close_functionality()
    else:
        if page.status_code == 200:
            subprocess.call(
                "start chrome.exe --new-window --start-maximized https://meet.lync.com/wwsiedupl/wwsi365/O0GEDZCD",
                shell=True)
            main_functionality()
            close_functionality()


# assign day number
actual_date = datetime.datetime.now()  # pobieramy aktualną date
actual_weekday_number = actual_date.weekday()


# Monday
if actual_weekday_number == 0:
    main_window.title("iConnect D202")
    main_window.geometry("260x350")
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="iConnect - bo mi sie nie chcialo klikac")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    Button1 = Button(main_window, text="Matematyka Dyskretna I wyk. - Zaikin", command=zaikin_commmand)
    Button1.config(height=3, width=35, relief="flat")
    Button1.pack()
    Button2 = Button(main_window, text="Matematyka Dyskretna II wyk. - Gniazdowski", command=gniazdowski_commmand)
    Button2.config(height=3, width=35, relief="flat")
    Button2.pack()
    Button3 = Button(main_window, text="Metody programowania wyk. - Figielska", command=figielska_commmand)
    Button3.config(height=3, width=35, relief="flat")
    Button3.pack()
    Button4 = Button(main_window, text="Metody programowania lab. - Figielska", command=figielska_commmand)
    Button4.config(height=3, width=35, relief="flat")
    Button4.pack()
    INFO = Label(main_window, text="")
    INFO.pack(side=BOTTOM)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="Jakub Piotrowski ver 1.0 Windows")
    INFO.pack(side=BOTTOM)
    main_window.mainloop()


# Tuesday
if actual_weekday_number == 1:
    main_window.title("iConnect")
    main_window.geometry("260x350")
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="iConnect - bo mi sie nie chcialo klikac")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    Button1 = Button(main_window, text="Matematyka Dyskretna I lab. - Rudak", command=rudak_command)
    Button1.config(height=3, width=35, relief="flat")
    Button1.pack()
    Button2 = Button(main_window, text="Podstawy Fizyki wyk. - Drazba", command=drazba_commmand)
    Button2.config(height=3, width=35, relief="flat")
    Button2.pack()
    Button3 = Button(main_window, text="Architekura OS wyk. - Chaladyniuk", command=chaladyniak_commmand)
    Button3.config(height=3, width=35, relief="flat")
    Button3.pack()
    Button4 = Button(main_window, text="Architekura OS lab. - Chaladyniuk", command=chaladyniak_commmand)
    Button4.config(height=3, width=35, relief="flat")
    Button4.pack()
    INFO = Label(main_window, text="")
    INFO.pack(side=BOTTOM)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="Jakub Piotrowski ver 1.0 Windows")
    INFO.pack(side=BOTTOM)
    main_window.mainloop()

# Wednesday
if actual_weekday_number == 2:
    main_window.title("iConnect D202")
    main_window.geometry("260x350")
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="iConnect - bo mi sie nie chcialo klikac")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    Button1 = Button(main_window, text="Analiza matematyczna wyk. - WINNI", command=winnicki_commmand)
    Button1.config(height=3, width=35, relief="flat")
    Button1.pack()
    Button2 = Button(main_window, text="Analiza matematyczna lab. - WINNI", command=winnicki_commmand)
    Button2.config(height=3, width=35, relief="flat")
    Button2.pack()
    Button3 = Button(main_window, text="Matematyka Dyskretna II lab. - Gniazdowski", command=gniazdowski_commmand)
    Button3.config(height=3, width=35, relief="flat")
    Button3.pack()
    INFO = Label(main_window, text="")
    INFO.pack(side=BOTTOM)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="Jakub Piotrowski ver 1.0 Windows")
    INFO.pack(side=BOTTOM)
    main_window.mainloop()

# Friday
if actual_weekday_number == 4:
    main_window.title("iConnect D202")
    main_window.geometry("260x350")
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="iConnect - bo mi sie nie chcialo klikac")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    Button1 = Button(main_window, text="Systemy operacyjne wyk. - Lewicki", command=lewicki_commmand)
    Button1.config(height=3, width=35, relief="flat")
    Button1.pack()
    Button2 = Button(main_window, text="Systemy operacyjne lab. - Lewicki", command=lewicki_commmand)
    Button2.config(height=3, width=35, relief="flat")
    Button2.pack()
    Button3 = Button(main_window, text="Język angielski lab. - Szewczyk", command=szewczyk_commmand)
    Button3.config(height=3, width=35, relief="flat")
    Button3.pack()
    Button4 = Button(main_window, text="Podstawy fizyki lab. - Kopcial", command=kopcial_commmand)
    Button4.config(height=3, width=35, relief="flat")
    Button4.pack()
    INFO = Label(main_window, text="")
    INFO.pack(side=BOTTOM)
    INFO = Label(main_window, text="")
    INFO.pack(side=TOP)
    INFO = Label(main_window, text="Jakub Piotrowski ver 1.0 Windows")
    INFO.pack(side=BOTTOM)
    main_window.mainloop()

