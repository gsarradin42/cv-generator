import os

import yaml


def load_yaml(folder: str, filename: str):
    with open(os.path.join(folder, filename), "r") as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
