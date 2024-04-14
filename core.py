import json
from typing import Any, Callable, Dict, List, Union

from config import SAVE_FILE_PATH

COMMANDS: Dict[str, Dict[str, Any]] = {}

def command(
        name: Union[str, None] = None,
        description: Union[str, None] = None,
        alt_names: Union[List[str], None] = None
    ):
    def decorator(func: Callable):
        _name = (name or func.__name__).replace(" ", "-").replace("_", "-")
        if _name not in COMMANDS:
            COMMANDS[_name] = {
                "func": func,
                "description": description,
                "alt_name": alt_names
            }

        return func

    return decorator


def run_command(name: str, *args):
    for _, cmd_data in COMMANDS.items():
        if name in (cmd_data["name"], *cmd_data["alt_names"]):
            cmd_data["func"](*args)
            return


def save():
    data = {}
    with open(SAVE_FILE_PATH, "w") as f:
        json.dump(data, f)


def load():
    ...

