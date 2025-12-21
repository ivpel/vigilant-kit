import os
import yaml
from pathlib import Path
from vigilant.logger import logger as log


def set_env_variables_from_dict(data):
    for key, value in data.items():
        os.environ[key] = str(value)

def set_env_variables_from_yaml(yaml_path):
    with open(yaml_path, 'r') as file:
        configs = yaml.safe_load(file)

    selenium_config = configs.get('vgl', {})
    set_env_variables_from_dict(selenium_config)


CONFIG_YAML_FILE = 'vgl.yaml'

def load_config_from_yaml(yaml_path: str = CONFIG_YAML_FILE, raise_on_missing: bool = False) -> bool:
    """
    Load environment variables from a YAML file.

    :param yaml_path: path to the yaml configuration file
    :param raise_on_missing: whether to raise if file is missing
    :return: True if configuration was loaded, False otherwise
    """
    config_path = Path(yaml_path)
    if not config_path.exists():
        message = f"Could not find `{yaml_path}` configuration file."
        if raise_on_missing:
            raise FileNotFoundError(message)
        log.warning(message)
        log.warning("If you don't want to use the yaml configuration file, ensure you provide all configuration data as environment variables.")
        return False

    log.info(f"Setting configuration from {yaml_path} file.")
    set_env_variables_from_yaml(yaml_path)
    return True
