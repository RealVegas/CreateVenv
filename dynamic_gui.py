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
                       'fieldbackground': '#323232',
                       'foreground': '#FFFFFF',
                       'relief': 'flat'}
        ),
        'TButton': dict(
                configure={'background': '#323232',
                           'relief': 'solid',
                           'foreground': '#FFFFFF',

                           }
        )
    })


# Создание окна
root: tk = tk.Tk()
root.title('Создание Python virtual environment GUI')

# Ширина и высота окна
win_width = 640
win_height = 480

scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

# Вычисляем координаты для размещения окна в центре
x_pos = (scr_width // 2) - (win_width // 2)
y_pos = (scr_height // 2) - (win_height // 2)

# Устанавливаем размер и положение окна
root.geometry(f'{win_width}x{win_height}+{x_pos}+{y_pos}')

apply_style()

# for style_name, style_properties in styles.items():
#     style.configure(style_name, **style_properties)

icon = PhotoImage(file='icons/main_icon.png')
root.iconphoto(False, icon)

frame: ttk = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Добавление виджетов
path_label: ttk = ttk.Label(frame, text='Задайте размещение нового виртуального окружения', anchor='center')
path_label.place(x=120, y=5, width=400, height=22)

task_font: tuple[str, int] = ('Arial', 11)  # через стили в settings={} не работало не смог понять почему

task_entry = ttk.Entry(frame, font=task_font)
task_entry.place(x=5, y=30, width=600, height=25)

add_button: ttk = ttk.Button(frame, text='...')
add_button.place(x=610, y=30, width=25, height=25)


























root.mainloop()