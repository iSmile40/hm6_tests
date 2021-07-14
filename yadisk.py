import requests


def create_folder(folder_name):
    token = ""
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": f"{folder_name}"}
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", params=params, headers=headers)
    if response.status_code == 201:
        print(f"Папка {folder_name} успешно создана")
    elif response.status_code == 409:
        print(f"Папка с названием '{folder_name}' была создана ранее")
    return response


def check_folder_exist(folder_name):
    token = ""
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": f"{folder_name}"}
    response = requests.get("https://cloud-api.yandex.net/v1/disk/resources", params=params, headers=headers)
    if response.status_code == 200:
        print("Папка с таким названием уже хранится на диске")
    elif response.status_code == 404:
        print("Папки с таким названием не существует")
    return response


create_folder("Homework")
check_folder_exist("Homework")
