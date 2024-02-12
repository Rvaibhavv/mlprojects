import zipfile
import os


def dataunzip(path,name):
    path =f"C:/Users/rvaib/Downloads/{path}"
    unzip_path = f"C:/Users/rvaib/onedrive/desktop/mlprojects/datasets/{name}"
    os.makedirs(unzip_path,exist_ok=True)
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)