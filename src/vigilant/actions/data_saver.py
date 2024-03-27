import csv
import xml.etree.ElementTree as ET
import os


def ensure_dir_exists(path):
    os.makedirs(path, exist_ok=True)


class DataSaver:

    def save_data_to_csv(self, data, filename, base_dir, mode='a'):
        ensure_dir_exists(base_dir)
        path = os.path.join(base_dir, f"{filename}.csv")
        with open(path, mode=mode, newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        print(f"Data successfully appended to {path}")

    def save_data_to_xml(self, data, filename, base_dir, root_element_name="Data", row_element_name="Row"):
        ensure_dir_exists(base_dir)
        path = os.path.join(base_dir, f"{filename}.xml")
        if os.path.exists(path):
            tree = ET.parse(path)
            root = tree.getroot()
        else:
            root = ET.Element(root_element_name)
            tree = ET.ElementTree(root)

        for row in data:
            row_element = ET.SubElement(root, row_element_name)
            for key, value in row.items():
                child = ET.SubElement(row_element, key)
                child.text = str(value)

        tree.write(path, encoding='utf-8', xml_declaration=True)
        print(f"Data successfully appended to {path}")

    def save_data_to_txt(self, data, filename, base_dir, mode='a'):
        ensure_dir_exists(base_dir)
        path = os.path.join(base_dir, f"{filename}.txt")
        with open(path, mode=mode, encoding='utf-8') as file:
            for line in data:
                file.write(f"{line}\n")
        print(f"Data successfully appended to {path}")
