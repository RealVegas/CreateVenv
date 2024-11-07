import os
import venv
import subprocess
import sys
import winreg


def is_python_installed():
    try:
        subprocess.check_output(['python', '--version'])
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

if is_python_installed():
    print("Python установлен.")
else:
    print("Python не установлен.")













def create_virtual_environment(env_name) -> None:

    env_path: str = os.path.join(os.getcwd(), env_name)

    # Создаем виртуальное окружение
    venv.create(env_path, with_pip=True)
    print(f'Виртуальное окружение {env_name} создано в {env_path}')

    # Определяем путь к pip в виртуальном окружении
    if os.name == 'nt':
        pip_executable = os.path.join(env_path, 'Scripts', 'pip')
    else:
        pip_executable = os.path.join(env_path, 'bin', 'pip')

    # Устанавливаем или обновляем pip, setuptools и wheel
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([pip_executable, 'install', '--upgrade', 'setuptools', 'wheel'])

if __name__ == "__main__":

    is_python_installed()

    # Путь к Python из реестра Windows
    key_read = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Python\\PythonCore\\')

    index = 0
    versions = []
    while True:
        try:
            # Перечисляем подключи
            subkey_name = winreg.EnumKey(key_read, index)
            versions.append(subkey_name)
            index += 1
        except OSError:
            # Когда больше нет подключей, будет выброшено исключение
            break
        # Закрываем ключ реестра
        winreg.CloseKey(key_read)

        # Получаем список версий Python
        print("Установленные версии Python:", versions)


    # Удалите пути виртуального окружения из PATH
    # Это может потребовать корректировки для вашей конкретной ситуации
    # venv_path = '/path/to/your/venv/bin'
    # os.environ['PATH'] = os.pathsep.join(
    #         p for p in os.environ['PATH'].split(os.pathsep) if not p.startswith(venv_path)
    # )
    #
    # try:
    #     # Найдите системный Python
    #     system_python = subprocess.check_output(['which', 'python']).decode().strip()
    #     print(f"Системный Python: {system_python}")
    # finally:
    #     # Восстановите оригинальный PATH
    #     os.environ['PATH'] = original_path


    # Задаем имя виртуального окружения
    # env_name = "myenv"

    # Создаем виртуальное окружение и устанавливаем необходимые пакеты
    # create_virtual_environment(env_name)