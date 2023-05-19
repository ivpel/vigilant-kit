import os
import json
from dotenv import load_dotenv, find_dotenv


def check_env_variables_exist(variables):
    missing_variables = []
    for variable in variables:
        if variable not in os.environ:
            missing_variables.append(variable)

    if missing_variables:
        raise ValueError(f"Environment variables are missing: {', '.join(missing_variables)}")

    return True


def check_json_file_exist(filename):
    current_dir = os.getcwd()

    while True:
        for root, dirs, files in os.walk(current_dir):
            if filename in files:
                return True

        parent_dir = os.path.dirname(current_dir)
        # Check if reached the root directory
        if current_dir == parent_dir:
            break
        current_dir = parent_dir

    return False


def find_json_file(filename):
    current_dir = os.getcwd()

    while True:
        for root, dirs, files in os.walk(current_dir):
            if filename in files:
                return os.path.join(root, filename)

        parent_dir = os.path.dirname(current_dir)
        # Check if reached the root directory
        if current_dir == parent_dir:
            break
        current_dir = parent_dir

    return None


def set_env_variables_from_json(filename):
    json_file_path = find_json_file(filename)
    if json_file_path is None:
        print(f"JSON file '{filename}' not found in the project's root directory or its subdirectories.")
        return

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for key, value in data.items():
        os.environ[key] = str(value)


env_variables = ['BASE_URL', 'SELENIUM_HOST', 'SELENIUM_BROWSER', 'WAIT_TIMEOUT', 'LOGGER_LEVEL']
json_configuration_file = 'vigilant.json'
env_configuration_file = '.vigilant.env'

if find_dotenv(env_configuration_file):
    print("Setting configuration from .vigilant.env file.")
    load_dotenv(env_configuration_file)
elif check_json_file_exist(json_configuration_file):
    print("Setting configuration from .vigilant.json file.")
    set_env_variables_from_json(json_configuration_file)
else:
    print("Could not find nor `.vigilant.env` nor `vigilant.json` configuration files.")
    print("If you don't want to use `.vigilant.env` nor `vigilant.json` configuration files - make sure, "
          "that you provide all configuration data as environment variables through  the way that is acceptable for "
          "you (pipeline configuration, custom bash script, etc.).")
    if check_env_variables_exist(env_variables):
        print("All mandatory environment variables exist.")
