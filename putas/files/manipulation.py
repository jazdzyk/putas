import os
import os.path as op
import random
import shutil
from typing import Callable

from tqdm import tqdm

from generators import path_generator
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


def remove_non_ascii_characters_in_dir_names(src_dir: str) -> None:
    count = 0

    for dir_path, dir_name in tqdm(path_generator(src_dir, with_name=True)):
        if not op.isdir(dir_path):
            continue

        is_non_ascii = [not (0 <= ord(c) <= 127) for c in dir_name]
        if any(is_non_ascii):
            new_name = ""

            for _is_non_ascii, c in zip(is_non_ascii, dir_name):
                if _is_non_ascii:
                    continue
                new_name += c

            os.rename(dir_path, op.join(src_dir, new_name))

            count += 1

    print(f"Successfully removed non-ASCII characters, renaming {count} files.")
