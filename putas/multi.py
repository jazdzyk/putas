from multiprocessing import Process
from multiprocessing.pool import ThreadPool
from typing import Callable, Iterable, Any


class Multiprocessor:

    def __init__(self, *func: Callable[[], None]):
        self._processes = [Process(target=_func) for _func in func]

    def run(self):
        for process in self._processes:
            process.start()

        for process in self._processes:
            process.join()


def simple_thread_pool_map(func: Callable[[Any], Any], iterable: Iterable, thread_num: int = None) -> Iterable:
    with ThreadPool(processes=thread_num) as pool:
        return pool.map(func, iterable)
