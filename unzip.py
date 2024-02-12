import zipfile
import os
path_of_zip ="C:/Users/rvaib/Downloads/titanic.zip"
name_of_dataset ="titanic1"

unzip_path = f"C:/Users/rvaib/onedrive/desktop/mlprojects/datasets/{name_of_dataset}"
os.makedirs(unzip_path,exist_ok=True)
with zipfile.ZipFile(path_of_zip, 'r') as zip_ref:
    zip_ref.extractall(unzip_path)
