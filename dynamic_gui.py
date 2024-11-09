import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.filedialog import askdirectory as ask_path

# Задание стилей для виджетов
def apply_style():
    style = ttk.Style()

    style.theme_use('clam')

    style.theme_settings('clam', settings={
        'TFrame': dict(
            configure={'background': '#282828'}
        ),
        'TLabel': dict(
            configure={'background': '#282828',
                       'foreground': '#FFFFFF',
                       'font': ('Arial', 11)}
        ),
        'TEntry': dict(
            configure={'background': '#282828',
                       'fieldbackground': '#282828',
                       'foreground': '#FFFFFF',
                       'relief': 'flat'}
        ),
        'TButton': dict(
            configure={
                'borderwidth': '1',
                'relief': 'solid',
                'font': ('Arial', 11),
                'foreground': '#FFFFFF',
            },
            map={
                'background': [('!active', '#282828'), ('active', '#323232')],
                'foreground': [('!active', '#FFFFFF'), ('active', '#FFFFFF')],
            }
        )
    })


# Создание окна
root: tk = tk.Tk()
root.title('Создание Python virtual environment GUI')
# root.tk.call('tk', 'scaling', 1.0)

# Размещение окна в центре экрана
win_width = 800
win_height = 335

scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

x_pos = (scr_width // 2) - (win_width // 2)
y_pos = (scr_height // 2) - (win_height // 2)

root.geometry(f'{win_width}x{win_height}+{x_pos}+{y_pos}')

# Иконка окна
icon = PhotoImage(file='images/main_icon.png')
root.iconphoto(False, icon)

# Фоновое изображение
background = PhotoImage(file='images/background.png')

canvas = tk.Canvas(root, width=800, height=335)
canvas.pack(fill="both", expand=True)

# Установите изображение в холст
canvas.create_image(0, 0, image=background, anchor="nw")






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
# add_button: ttk = ttk.Button(frame, text='...')
# add_button.place(x=610, y=30, width=25, height=25)


























root.mainloop()