import tkinter as tk
from tkinter import ttk
import time

def pomodoro(focus_time, break_time, cycles):
    for i in range(cycles):
        print(f'Start working - cycle {i+1}')
        seconds = focus_time * 60
        while seconds:
            minutes, seconds = divmod(seconds, 60)
            focus_label.config(text=f"Focus Time Remaining: {minutes:02d}:{seconds:02d}")
            root.update()
            seconds -= 1
            time.sleep(1)
        print("Time's up! Take a break.")
        focus_label.config(text=f"Focus Time Remaining: 00:00")
        root.update()
        
        seconds = break_time * 60
        while seconds:
            minutes, seconds = divmod(seconds, 60)
            break_label.config(text=f"Break Time Remaining: {minutes:02d}:{seconds:02d}")
            root.update()
            seconds -= 1
            time.sleep(1)
            print("Break's over! Back to work.")
        break_label.config(text=f"Break Time Remaining: 00:00")
        root.update()

def start_pomodoro():
    focus_time = int(focus_entry.get())
    break_time = int(break_entry.get())
    cycles = int(cycles_entry.get())
    cycles_label.config(text=f"Cycles remaining: {cycles}")
    root.update()
    pomodoro(focus_time, break_time, cycles)

root = tk.Tk()
root.title("Pomodoro Timer")

style = ttk.Style()
style.theme_use("clam")

focus_label = ttk.Label(root, text="Focus Time Remaining: 00:00")
focus_label.grid(row=0, column=0)
focus_entry = ttk.Entry(root)
focus_entry.grid(row=0, column=1)

break_label = ttk.Label(root, text="Break Time Remaining: 00:00")
break_label.grid(row=1, column=0)
break_entry = ttk.Entry(root)
break_entry.grid(row=1, column=1)

cycles_label = ttk.Label(root, text="Cycles remaining: ")
cycles_label.grid(row=2, column=0)
cycles_entry = ttk.Entry(root)
cycles_entry.grid(row=2, column=1)

start_button = ttk.Button(root, text="Start", command=start_pomodoro)
start_button.grid(row=3, column=1)

root.mainloop()