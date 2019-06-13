from json import load
from pathlib import Path


def load_config():
    """ Load config info from JSON file """
    path = Path('config.json')
    if not path.exists():
        raise FileNotFoundError('Config file not found!')

    with path.open(mode='r') as fl:
        config = load(fl)

    return config
