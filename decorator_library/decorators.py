from time import sleep
from typing import Callable

from httpx import TimeoutException


def retry(func: Callable):
    def inner():
        retries = 0
        while retries != 5:
            try:
                func()
            except TimeoutException:
                sleep(0.2)
                continue

    return inner
