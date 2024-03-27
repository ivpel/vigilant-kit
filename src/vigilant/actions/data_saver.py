import csv
import xml.etree.ElementTree as ET
import os


def ensure_dir_exists(path):
    os.makedirs(path, exist_ok=True)


class DataSaver:

    def save_data_to_txt(self, data, filename, base_dir, mode='a'):
        ensure_dir_exists(base_dir)
        path = os.path.join(base_dir, f"{filename}.txt")
        with open(path, mode=mode, encoding='utf-8') as file:
            file.write(f"{data}\n")
        print(f"Data successfully appended to {path}")
