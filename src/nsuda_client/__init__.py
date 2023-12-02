import dearpygui.dearpygui as dpg
from pathlib import Path
from config import is_development
from build import RESOURCE_FOLDER
import platform

width = 300
height = 400

icon_name: str = None

if platform.system() == "Windows":
    icon_name = "Logo.ico"
elif platform.system() == "Darwin":
    icon_name = "Logo.png"

dpg.create_context()
if is_development:
    path = (Path(__file__).parent / "resource" / icon_name).absolute().as_posix()
else:
    path = (Path(__file__).parent.parent / RESOURCE_FOLDER / icon_name).absolute().as_posix()

dpg.create_viewport(title='NSUDA', 
                    width=width, 
                    height=height, 
                    small_icon=path, 
                    large_icon=path, 
                    resizable=False,
                    x_pos=700,
                    y_pos=400)
dpg.setup_dearpygui()
dpg.show_viewport()
