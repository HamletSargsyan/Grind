import json
import time
from typing import Any, Callable, Dict, List, Union

from config import SAVE_FILE_PATH

COMMANDS: Dict[str, Dict[str, Any]] = {}
GAME_DATA: Dict[str, Any] = {}

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


class GameDataDict():
    player_name: str = "Catalyst"
    money: int = 0
    level: int = 1
    timestamp: float = time.time()

    res_time = {
        "seconds": 0,
        "minutes": 0,
        "hours": 0,
        "wait_seconds": 0,
        "wait_minutes": 0,
        "wait_hours": 0,
    }

    res_stone = {
        "name": "Камень",
        "count": 0,
        "price": 1,
        "price_start": 1,
        "up_cost": 10,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_wood = {
        "name": "Дерево",
        "count": 0,
        "price": 5,
        "price_start": 5,
        "up_cost": 100,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_coal = {
        "name": "Уголь",
        "count": 0,
        "price": 50,
        "price_start": 50,
        "up_cost": 500,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_fabric = {
        "name": "Ткань",
        "count": 0,
        "price": 100,
        "price_start": 100,
        "up_cost": 1000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_copper = {
        "name": "Медь",
        "count": 0,
        "price": 200,
        "price_start": 200,
        "up_cost": 2000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_steel = {
        "name": "Железо",
        "count": 0,
        "price": 500,
        "price_start": 500,
        "up_cost": 4000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_gold = {
        "name": "Золото",
        "count": 0,
        "price": 1000,
        "price_start": 1000,
        "up_cost": 10000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_uranium = {
        "name": "Уран",
        "count": 0,
        "price": 2000,
        "price_start": 2000,
        "up_cost": 50000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_klit = {
        "name": "Кремнелит",
        "count": 0,
        "price": 5000,
        "price_start": 5000,
        "up_cost": 100000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_chromium = {
        "name": "Хром",
        "count": 0,
        "price": 10000,
        "price_start": 10000,
        "up_cost": 500000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    colors = [
        {"name": "Белый", "up_cost": 10000, "per_s": 100000, "level": 0},
        {"name": "Серый", "up_cost": 10000, "per_s": 200000, "level": 0},
        {"name": "Красный", "up_cost": 10000, "per_s": 300000, "level": 0},
        {"name": "Желтый", "up_cost": 10000, "per_s": 400000, "level": 0},
        {"name": "Зеленый", "up_cost": 10000, "per_s": 500000, "level": 0},
        {"name": "Бирюзовый", "up_cost": 10000, "per_s": 600000, "level": 0},
        {"name": "Синий", "up_cost": 10000, "per_s": 700000, "level": 0},
        {"name": "Фиолетовый", "up_cost": 10000, "per_s": 800000, "level": 0},
        {"name": "Черный", "up_cost": 10000, "per_s": 900000, "level": 0},
        {"name": "Блестки", "up_cost": 10000, "per_s": 1000000, "level": 0},
    ]

    

def save():
    with open(SAVE_FILE_PATH, "w") as f:
        json.dump(GAME_DATA, f)


def load():
    global GAME_DATA
    with open(SAVE_FILE_PATH, "r") as f:
        GAME_DATA = json.load(f)
