from typing import Final
from prompt_toolkit import PromptSession


prompt_session = PromptSession("Действие  : ")

_prompt_session: Final = prompt_session


def init_session():
    global prompt_session
    prompt_session = _prompt_session
