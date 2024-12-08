import tkinter as tk
import threading
import random
import time
from PIL import Image, ImageTk
dialog_count = 0

def show_singer_message():
    global dialog_count
    dialog_count += 1
    win = tk.Toplevel(root)
    win.title("Hài thiệt chứ hả")
    x = random.randint(0, root.winfo_screenwidth() - 300)
    y = random.randint(0, root.winfo_screenheight() - 150)
    win.geometry(f"300x150+{x}+{y}")
    win.configure(bg="pink")

    frame = tk.Frame(win, bg="pink", highlightbackground="white", highlightcolor="pink")
    frame.pack(expand=True, fill='both', padx=15, pady=15)
    
    label = tk.Label(frame, text="Cảm ơn các bạn đã xem.", font=("Helvetica", 15, "bold"), bg="pink") 
    label.pack(expand=True, anchor="center")

    def close_dialog(win):
        global dialog_count
        win.destroy()
        dialog_count -= 1
        if dialog_count == 0:
            root.grab_release()

    win.protocol("WM_DELETE_WINDOW", lambda: close_dialog(win))
    win.grab_set()

def show_message():
    def task():
        for _ in range(200):
            show_singer_message()
            time.sleep(0.1)
    threading.Thread(target=task).start()

root = tk.Tk()
root.title("Code phong bạt")
root.geometry("600x528")
background_image_path = 'Improve/heart.png' 
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(root, width=600, height=528)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=background_photo, anchor='nw')

button_style = {
    "bg": "pink",
    "fg": "black",
    "font": ("Helvetica", 14, "bold"),
    "relief": "raised",
    "borderwidth": 3,
    "width": 20,
    "height": 2
}

button = tk.Button(root, text="COI CHỪNG VIRUT ĐẤY!!!", command=show_message, **button_style)
canvas.create_window(300, 200, window=button) 

root.mainloop()