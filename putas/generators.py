import os
import os.path as op
from typing import Iterator, Tuple, Union, Generator


def path_generator(dir_path: str, with_name=False) -> Iterator[Union[str, Tuple[str, str]]]:
    """
    Generates paths for files in a given directory.
    Provides the same functionality as `os.listdir()`, but builds full file paths, not only file names.

    :param dir_path: a path to directory
    :param with_name: a flag whether to return a file name, too, or only a file path (default: False)
    :return: an iterated file path
    """
    for file_name in os.listdir(dir_path):
        output = op.join(dir_path, file_name)

        if with_name:
            output = (output, file_name)

        yield output


def empty_lists(n: int) -> Generator[list, None, None]:
    return ([] for _ in range(n))
