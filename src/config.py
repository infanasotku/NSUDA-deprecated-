import sys
from pathlib import Path
from build import RESOURCE_FOLDER
import nsuda_client.win as win

is_development: bool = False

if getattr(sys, 'frozen', False):
    is_development = False
else:
    is_development = True

resource_path: str = None
app_folder_path: str = None
login_file_name = ".NSUDA_login"
if is_development:
    resource_path = (Path(__file__).parent / "nsuda_client" / "resource").absolute().as_posix()
    app_folder_path = (Path(__file__).parent).absolute().as_posix()
else:
    resource_path = (Path(__file__).parent / RESOURCE_FOLDER).absolute().as_posix()
    app_folder_path = str(Path.home())
    
window_width = 500
window_height = 400

input_field_width = 350

width_shift = 0
height_shift = 0

version = "1.0.1a"

import platform

if platform.system() == "Windows":
    width_shift = win.width_shift
    height_shift = win.height_shift