import json
from typing import Callable, Union


COMMANDS = {}

def command(name: Union[str, None] = None):
    def decorator(func: Callable):
        _name = (name or func.__name__).replace(" ", "-").replace("_", "-")
        if _name not in COMMANDS:
            COMMANDS[_name] = func

        return func
    return decorator


def save():
    ...

def load():
    ...