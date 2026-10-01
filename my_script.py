from json import dump
from os import path
from platform import system, release, version, platform, machine

def get_info():
    os_name = system()

    if os_name == "Windows":
        os_name = "Windows"
    elif os_name == "Linux":
        os_name = "Linux"
    elif os_name == "Darwin":
        os_name = "macOS"
    else:
        os_name = "Не определена"

    return {
        "operating_system": os_name,
        "release": release(),
        "version": version(),
        "platform": platform(),
        "architecture": machine()
    }

def save_json(data):
    file_path = path.join(
        path.dirname(path.abspath(__file__)),
        "os_info.json"
    )

    with open(file_path, "w", encoding="utf-8") as file:
        dump(data, file, indent=4, ensure_ascii=False)

    return file_path

info = get_info()
file_path = save_json(info)

print("Информация успешно сохранена!")
print(f"Файл: {file_path}")
print(f"Операционная система: {info['operating_system']}")
