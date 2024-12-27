import os
import yaml
from pathlib import Path

RED = "\033[31m"
RESET = "\033[0m"

def set_env_variables_from_dict(data):
    for key, value in data.items():
        os.environ[key] = str(value)

def set_env_variables_from_yaml(yaml_path):
    with open(yaml_path, 'r') as file:
        configs = yaml.safe_load(file)

    selenium_config = configs.get('vgl', {})
    set_env_variables_from_dict(selenium_config)


CONFIG_YAML_FILE = 'vgl.yaml'

if Path(CONFIG_YAML_FILE).exists():
    print(f"Setting configuration from {CONFIG_YAML_FILE} file.")
    set_env_variables_from_yaml(CONFIG_YAML_FILE)
else:
    print(f"{RED}Could not find `{CONFIG_YAML_FILE}` configuration file.{RESET}")
    print(f"{RED}If you don't want to use the yaml configuration file, ensure you provide all configuration data as environment variables.{RESET}")
