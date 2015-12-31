import os
import sys
import yaml


CONFIG_FILE = "app_settings.yaml"
_config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), CONFIG_FILE)
config = yaml.load(open(_config_path, 'r'))
