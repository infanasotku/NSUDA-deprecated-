import dearpygui.dearpygui as dpg
import nsuda_client.event as event
from nsuda_client import width, height

with dpg.window(tag="Primary Window") as main_window:
    dpg.add_input_text(tag="connect_item",
                       hint="Input email",
                       pos=(width // 2 - 105, height // 2 - 40),
                       width=200
                       )
    connect_button = dpg.add_button(label="Connect", 
                   callback=event.connect_button_clicked,
                   pos=(width // 2 - 55, height // 2 - 10), 
                   width=100, height=20,
                   tag="connect_button"
                   )
    disconnect_button = dpg.add_button(label="Disconnect", 
                   callback=event.disconnect_button_clicked,
                   pos=(width // 2 - 55, height // 2 - 10), 
                   width=100, height=20,
                   tag="disconnect_button",
                   show=False
                   )

dpg.set_primary_window("Primary Window", True)



def start_nsuda():
    dpg.start_dearpygui()
    dpg.destroy_context()

