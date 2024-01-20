import dearpygui.dearpygui as dpg
from config import resource_path, window_height, window_width, version
import platform



icon_name: str = None

if platform.system() == "Windows":
    icon_name = "Logo.ico"
elif platform.system() == "Darwin":
    icon_name = "Logo.png"
elif platform.system() == "Linux":
    icon_name = "Logo.png"


dpg.create_context()

dpg.create_viewport(title='NSUDA v' + version, 
                    width=window_width, 
                    height=window_height, 
                    small_icon=resource_path + "/" + icon_name, 
                    large_icon=resource_path + "/" + icon_name, 
                    resizable=False,
                    x_pos=700,
                    y_pos=400)
dpg.setup_dearpygui()
dpg.show_viewport()
