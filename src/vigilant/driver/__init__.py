import os
import yaml
from pathlib import Path

def set_env_variables_from_dict(data):
    for key, value in data.items():
        os.environ[key] = str(value)

def set_env_variables_from_yaml(yaml_path):
    with open(yaml_path, 'r') as file:
        configs = yaml.safe_load(file)

    selenium_config = configs.get('selenium-configuration', {})
    set_env_variables_from_dict(selenium_config)

    # Handle credentials
    creds_file_path = configs.get('test-credentials', {}).get('file')
    if creds_file_path and Path(creds_file_path).exists():
        with open(creds_file_path, 'r') as creds_file:
            credentials = yaml.safe_load(creds_file)
        set_env_variables_from_dict(credentials)
    else:
        print(f"Credentials file '{creds_file_path}' not found.")

CONFIG_YAML_FILE = 'vgl_config.yaml'

if Path(CONFIG_YAML_FILE).exists():
    print(f"Setting configuration from {CONFIG_YAML_FILE} file.")
    set_env_variables_from_yaml(CONFIG_YAML_FILE)
else:
    print(f"Could not find `{CONFIG_YAML_FILE}` configuration file.")
    print("If you don't want to use the yaml configuration file, ensure you provide all configuration data as environment variables.")
