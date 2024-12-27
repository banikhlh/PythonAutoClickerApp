import keyboard
import pyautogui
import tkinter
import threading
import time


stop_event = threading.Event()
is_running = False


def toggle():
    global is_running
    if is_running:
        stop()
        btn['text'] = f"Start({default_hotkey.get()})"
    else:
        start()
        btn['text'] = f"Stop({default_hotkey.get()})"
    is_running = not is_running


def start():
    time.sleep(0.5)
    stop_event.clear()
    threading.Thread(target=click, daemon=True).start()


def click():
    while not stop_event.is_set():
        pyautogui.click()
        time.sleep(delay.get())


def stop():
    stop_event.set()


def update_hotkey():
    keyboard.remove_hotkey(current_hotkey[0])
    current_hotkey[0] = keyboard.add_hotkey(default_hotkey.get(), toggle)
    btn['text'] = f"Start({default_hotkey.get()})"


window = tkinter.Tk()
window.title('Clicker')
window.geometry('300x150')

default_hotkey = tkinter.StringVar(value='ctrl+shift+c')
delay = tkinter.DoubleVar(value=0.1)

tkinter.Label(window, text='Delay').pack()
tkinter.Entry(window, textvariable=delay).pack()

tkinter.Label(window, text='Hotkey').pack()
tkinter.Entry(window, textvariable=default_hotkey).pack()

tkinter.Button(window, text='Apply Hotkey', command=update_hotkey).pack()

btn = tkinter.Button(window, text=f"Start({default_hotkey.get()})", command=toggle)
btn.pack()

current_hotkey = [keyboard.add_hotkey(default_hotkey.get(), toggle)]

window.mainloop()
