from config import is_development
from build import XRAY_FOLDER
from pathlib import Path
import os
import platform

xray_path:str = None
arch_folder: str = platform.uname().machine
if is_development:
    xray_path = (Path(__file__).parent / arch_folder / "xray").absolute().as_posix()
else:
    xray_path = (Path(__file__).parent.parent.parent / arch_folder / XRAY_FOLDER / "xray").absolute().as_posix()
print(xray_path)

def load_env_setting():
    os.system("networksetup -setsocksfirewallproxy wi-fi localhost 2080")


def start_env():
    os.system("networksetup -setsocksfirewallproxystate wi-fi on")

def exit_env():
    os.system("networksetup -setsocksfirewallproxystate wi-fi off")
