import os
import subprocess
import sys
import winreg
from winreg import HKEYType

import tkinter


def global_python() -> str | None:
    if os.name != 'nt':
        print('Это программа предназначена только для Windows')
        print('Программа завершает свою работу')
        exit()

    # Открытие ключей реестра
    user_key: HKEYType = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE')
    machine_key: HKEYType = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE')

    key_index: int = -1
    find_python: str = 'not'

    while True:
        key_index += 1

        try:
            # Перебор подключей
            user_subkey: str = winreg.EnumKey(user_key, key_index)
            machine_subkey: str = winreg.EnumKey(machine_key, key_index)

            if user_subkey == 'Python':
                find_python: str = 'user'
                break

            elif machine_subkey == 'Python':
                find_python: str = 'machine'
                break

        except OSError:
            # Подключей больше нет
            break

    # Закрытие ключей
    winreg.CloseKey(user_key)
    winreg.CloseKey(machine_key)
    return find_python


def python_versions(location: str) -> list[str]:

    sub_key = 'SOFTWARE\\Python\\PythonCore\\'

    if location == 'not':
        print('На данной машине отсутствует установленный интерпретатор Python')
        print('Программа завершает свою работу')
        exit()

    elif location == 'user':
        main_key: HKEYType = winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key)

    elif location == 'machine':
        main_key: HKEYType = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key)

        py_index = -1
        py_version = []

        while True:
            py_index += 1

            try:
                # Перечисляем подключи
                version_name: str = winreg.EnumKey(main_key, py_index)
                py_version.append(version_name)

            except OSError:
                # Подключей больше нет
                break

        # Закрываем ключ реестра
        winreg.CloseKey(main_key)
        return py_version


def python_paths(location: str, py_vers: list[str]) -> dict[str, str]:

    folder_key: HKEYType = winreg.REG_NONE()
    result_dict: dict[str, str] = {}

    for one_key in py_vers:

        sub_key: str = f'SOFTWARE\\Python\\PythonCore\\{one_key}\\InstallPath'

        if location == 'user':
            folder_key: HKEYType = winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key, 0, winreg.KEY_READ)
        elif location == 'machine':
            folder_key: HKEYType = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key, 0, winreg.KEY_READ)

        python_folder, _ = winreg.QueryValueEx(folder_key, '')
        result_dict[one_key]: str = python_folder

    # Закрываем ключ реестра
    winreg.CloseKey(folder_key)
    return result_dict


def virtual_env(python_path: str, venv_name: str) -> None:

    # вместо os.getcwd() надо запросить у пользователя расположение через
    # метод tkinter: from tkinter.filedialog import askdirectory as ask_path
    #
    # Функция для получения пути к папке c виртуальным окружением
    # def get_path() -> Path:
    #     path: str = ask_path(title='new venv - Выберите папку', initialdir=os.getcwd())
    #
    #     if not path:
    #         print('В меню выбора папки была нажата кнопка "Отмена"')
    #         input('\nДля завершения программы нажмите Enter')
    #         exit()
    #
    #     return Path(path) -> пока буду обозначать как os.getcwd()

    venv_path: str = os.path.join(os.getcwd(), venv_name)

    if not os.path.exists(venv_path):
        os.makedirs(venv_path)

    subprocess.check_call([python_path, '-m', 'venv', venv_path])
    # Создаем виртуальное окружение

    print(f'Виртуальное окружение {venv_name} создано в {os.getcwd()}')

    # Определяем путь к pip в виртуальном окружении
    pip_exe = os.path.join(venv_path, 'Scripts', 'pip')

    # Устанавливаем или обновляем pip, setuptools и wheel
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([pip_exe, 'install', '--upgrade', 'setuptools', 'wheel'])


if __name__ == "__main__":

    py_key: str = global_python()
    py_ver: list[str] = python_versions(py_key)
    py_path: dict[str, str] = python_paths(py_key, py_ver)

    print(py_key)
    print(py_ver)

    for item_key, item_value in py_path.items():
        print(f'version: {item_key} | path: {item_value}')