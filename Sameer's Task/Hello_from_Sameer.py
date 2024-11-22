print("Hello Alexa")
print("Sameer here")
print("This is my first task submission")
import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')  
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  


root = tk.Tk()
root.title("Clock")


clock_label = tk.Label(root, font=('Helvetica', 48), background='black', foreground='white')
clock_label.pack(anchor='center')
update_time()
root.mainloop()
