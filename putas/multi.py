from multiprocessing import Process
from typing import Callable


class Multiprocessor:

    def __init__(self, *func: Callable[[], None]):
        self._processes = [Process(target=_func) for _func in func]

    def run(self):
        for process in self._processes:
            process.start()

        for process in self._processes:
            process.join()
