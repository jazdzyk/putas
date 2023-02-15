import os
import os.path as op
import random
import shutil
from typing import Callable

from tqdm import tqdm

from putas.files.io import load_json, save_json


def merge_jsons_in_dir(src_dir: str, out_path: str) -> None:
    """Merges all .json files in a given directory into one output .json file.

    :param src_dir: a directory containing input .json files
    :param out_path: a path to the merged .json file
    """
    all_data_dict = {}
    all_data_list = []

    for file_name in sorted(os.listdir(src_dir)):
        json_data = load_json(op.join(src_dir, file_name))

        if isinstance(json_data, list):
            for item in json_data:
                all_data_list.append(item)
        else:
            all_data_dict.update(json_data)

    save_json(all_data_dict or all_data_list, out_path)


_CopyMoveFunction = Callable[[str, str], None]


def move_n_random_files(src_dir: str, dst_dir: str, n: int) -> None:
    _copy_or_move_n_random_files(shutil.move, src_dir, dst_dir, n)


def copy_n_random_files(src_dir: str, dst_dir: str, n: int) -> None:
    _copy_or_move_n_random_files(shutil.copy2, src_dir, dst_dir, n)


def _copy_or_move_n_random_files(func: _CopyMoveFunction, src_dir: str, dst_dir: str, n: int) -> None:
    os.makedirs(dst_dir, exist_ok=True)

    file_names = os.listdir(src_dir)
    random.shuffle(file_names)

    n = min(n, len(file_names))

    for file_name in tqdm(file_names[:n]):
        func(op.join(src_dir, file_name), op.join(dst_dir, file_name))

    action = {
        shutil.copy2: "copied",
        shutil.move: "moved",
    }[func]

    print(f"Successfully {action} {n} files.")
