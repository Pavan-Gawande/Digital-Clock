import tkinter as tk
import time
from PIL import Image, ImageTk

win = tk.Tk()
win.title("Digital Clock")
win.geometry("640x360")

bg_image = Image.open('bg1.jpg')
bg_photo = ImageTk.PhotoImage(bg_image)

win.bg_photo = bg_photo

canvas = tk.Canvas(win, width=640, height=360)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=bg_photo, anchor="nw")

def update_clock():
    canvas.delete("time")
    
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%b %d, %Y")
    
    canvas.create_text(535, 265, text=current_time, fill="white", font=("Helvetica", 20, "bold"), tag="time")
    canvas.create_text(500, 310, text=current_date, fill="white", font=("Helvetica", 30, "bold"), tag="time")
    
    canvas.after(1000, update_clock)

update_clock()

win.mainloop()
