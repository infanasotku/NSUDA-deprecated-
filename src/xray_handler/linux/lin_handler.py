from config import is_development
from build import XRAY_FOLDER
from pathlib import Path
import os

xray_path:str = None

if is_development:
    xray_path = (Path(__file__).parent / "xray").absolute().as_posix()
else:
    xray_path = (Path(__file__).parent.parent.parent / XRAY_FOLDER / "xray").absolute().as_posix()

# For linux requires manual set up env.

def load_env_setting():
    pass


def start_env():
    pass

def exit_env():
    pass
