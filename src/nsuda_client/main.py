import dearpygui.dearpygui as dpg
from xray_handler.handler import Handler

dpg.create_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)



def start_nsuda():
    dpg.start_dearpygui()
    dpg.destroy_context()   