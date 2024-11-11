import tkinter as tk


# from tkinter import ttk
# from tkinter import PhotoImage
# from tkinter import I
# from tkinter.filedialog import askdirectory as ask_path


def on_action(event):
    if event.type == tk.EventType.Enter:
        label.config(image=ask_dir_act)
    elif event.type == tk.EventType.Leave:
        label.config(image=ask_dir_inact)
    elif event.type == tk.EventType.ButtonPress:
        label.config(image=ask_dir_press)
    elif event.type == tk.EventType.ButtonRelease:
        label.config(image=ask_dir_act)


# Создание окна
root: tk = tk.Tk()
root.title('Python virtual environment maker v.1.0')
root.resizable(False, False)
root.tk.call('tk', 'scaling', 1.0)

# Размещение окна в центре экрана
win_width = 800
win_height = 220

scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

x_pos = (scr_width // 2) - (win_width // 2)
y_pos = (scr_height // 2) - (win_height // 2)

root.geometry(f'{win_width}x{win_height}+{x_pos}+{y_pos}')

# Иконка окна и фоновое изображение
icon = tk.PhotoImage(file='images/main_icon.png')
background = tk.PhotoImage(file='images/background.png')

# Установка иконки и фона
root.iconphoto(False, icon)

backdrop_canvas = tk.Canvas(root, width=800, height=220)
backdrop_canvas.pack(fill='both', expand=True)
backdrop_canvas.create_image(0, 0, image=background, anchor="nw")

# Загрузка элементов интерфейса
ask_dir_inact = tk.PhotoImage(file='images/buttons/askdir_inact.png')
ask_dir_act = tk.PhotoImage(file='images/buttons/askdir_act.png')
ask_dir_press = tk.PhotoImage(file='images/buttons/askdir_press.png')

label = tk.Label(root, image=ask_dir_inact, borderwidth=0)


label.bind("<Enter>", on_action)
label.bind("<Leave>", on_action)
label.bind("<ButtonPress-1>", on_action)
label.bind("<ButtonRelease-1>", on_action)

# Создание кнопки

label.place(x=768, y=15)


# frame.create_image(0, 0, image=bkg, anchor='nw')


# Добавление виджетов
# path_label: ttk = ttk.Label(frame, text='Задайте размещение нового виртуального окружения', anchor='center')
# path_label.place(x=120, y=5, width=400, height=22)
#
# task_font: tuple[str, int] = ('Arial', 11)  # через стили в settings={} не работало не смог понять почему
#
# task_entry = ttk.Entry(frame, font=task_font)
# task_entry.place(x=5, y=30, width=600, height=25)
#
root.mainloop()