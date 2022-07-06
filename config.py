"""
This file handles parsing and passing on the config values set in config/default.yml
If you want to use another configuration file, it can be set globally with set_config
"""

import yaml
from pathlib import Path

configs_paths = Path("config")
configs = configs_paths.glob("**/*.yml")

config_dict = {}
for config in configs:
    config_dict[config.name] = yaml.safe_load(open(config))

config = yaml.safe_load(open("config/default.yml"))


def set_config(new_config_path):
    global config
    config = config_dict[new_config_path]
