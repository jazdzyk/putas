import json
from typing import Union, List

import yaml


def load_json(path: str) -> dict:
    """Loads data from a .json file.

    :param path: a path to a .json file
    :return: a dict with .json data
    """
    if not path.endswith(".json"):
        path += ".json"

    with open(path, "r") as label_json:
        return json.load(label_json)


def save_json(data: Union[dict, list], path: str, indent=4, ensure_ascii=True) -> None:
    """Saves given data to a .json file.

    :param data: a data to be saved
    :param path: a path to output .json file
    :param indent: an indentation size
    :param ensure_ascii: a flag whether to ensure ASCII formatting
    """
    if not path.endswith(".json"):
        path += ".json"

    with open(path, "w") as out_json:
        json.dump(data, out_json, indent=indent, ensure_ascii=ensure_ascii)


def load_yaml(path: str) -> dict:
    """Loads data from a .yaml file.

    :param path: a path to a .yaml file
    :return: a dict with .yaml data
    """
    if not path.endswith(".yaml"):
        path += ".yaml"

    with open(path, "r") as yaml_file:
        return yaml.safe_load(yaml_file)


def save_yaml(data: Union[dict, list], path: str) -> None:
    """Saves given data to a .json file.

    :param data: a data to be saved
    :param path: a path to output .yaml file
    """
    if not path.endswith(".yaml"):
        path += ".yaml"

    with open(path, "w") as out_yaml:
        yaml.dump(data, out_yaml, default_flow_style=False)


def load_txt(path: str, lines=False) -> Union[str, List[str]]:
    """Loads data from a .txt file.

    :param path: a path to a .txt file
    :param lines: a flag whether to read data as a list of lines (default = False)
    :return: a string or a list of strings with .txt data
    """
    if not path.endswith(".txt"):
        path += ".txt"

    with open(path, "r") as in_txt:
        return in_txt.readlines() if lines else in_txt.read()


def save_txt(data: str, path: str) -> None:
    """Saves given data to a .txt file.

    :param data: a string-like data to be saved
    :param path: a path to output .txt file
    """
    if not path.endswith(".txt"):
        path += ".txt"

    with open(path, "w") as out_txt:
        out_txt.write(data)
