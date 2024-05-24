import os
import sys
from typing import Union
from core import COMMANDS, command, save


@command("main", alt_names=["m"])
def main_cmd():
    ...


@command()
def help(cmd: str = "help"):
    if cmd not in COMMANDS:
        print(f"Команды `{cmd}` не существует")
    elif description := COMMANDS[cmd].get("description"):
        print(description)
    else:
        print(f"У комманды `{cmd}` нет документации")


@command("exit", alt_names=["e"])
def exit_cmd():
    os.system("clear")
    save()
    sys.exit(1)


@command("save")
def save_cmd():
    save()


@command()
def sell(r: Union[str, int]):
    ...


@command("open")
def open_cmd(name: str):
    ...


@command("up")
def up(r: Union[str, int], level: int = 1):
    ...


# TODO: add: number style [style]


@command()
def stats():
    ...


@command("name")
def name_cmd(name: str):
    ...


@command()
def delete_save(name: str):
    ...
