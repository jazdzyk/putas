import os
import os.path as op

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
