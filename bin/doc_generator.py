import os
import sys
import re
from pathlib import Path


def process_file(file_path):
    with open(file_path) as f:
        content = f.read()

    pattern = r'def\s+(\w+\([^)]*\))[^{]*?"""([^"""]*)"""'
    matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)

    functions = []

    for match in matches:
        func_name = match.group(1)
        if '__init__' in func_name:
            continue

        docstring = match.group(2)
        line_number = content[:match.start()].count('\n') + 1

        functions.append({
            'func_name': func_name,
            'docstring': docstring,
            'line_number': line_number,
            'file_path': file_path
        })

    return functions


def generate_md_docs(target_directory, output_file):
    all_functions = []

    for root, _, files in os.walk(target_directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                all_functions.extend(process_file(file_path))

    # Sort the functions alphabetically
    all_functions.sort(key=lambda x: x['func_name'])

    # Write the table of contents and the functions to the output file
    with open(output_file, "w") as f:
        f.write("# Table of Contents\n\n")
        for func in all_functions:
            func_name = func['func_name']
            anchor = func_name.replace("(", "").replace(")", "").replace(",", "").replace(" ", "")
            f.write(f"- [{func_name}](#{anchor})\n")
        f.write("\n")

        for func in all_functions:
            func_name = func['func_name']
            docstring = func['docstring']
            line_number = func['line_number']
            file_path = func['file_path']

            f.write(f"## {func_name}\n\n")
            f.write(f"{docstring}\n\n")

            f.write(
                f"```python\n# {file_path} (line {line_number})\ndef {func_name} -> return_type:\n    \"\"\"{docstring}\"\"\"\n    # Function code goes here\n```\n\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <target_directory>")
        sys.exit(1)

    target_directory = Path(sys.argv[1])
    output_file = "../documentation.md"

    # Remove existing output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    generate_md_docs(target_directory, output_file)
