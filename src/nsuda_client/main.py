import dearpygui.dearpygui as dpg
import nsuda_client.event as event
from config import *


def configure_nsuda():
    with dpg.font_registry():
        default_font = dpg.add_font(resource_path + "/Gill Sans.ttf", 30)
        event.small_font = dpg.add_font(resource_path + "/Gill Sans.ttf", 21)
        dpg.bind_font(default_font)
    with dpg.window(tag="Primary Window"):
        email, password = None, None
        try:
            with open("login", "r") as f:
                email, password = f.read().split()
        except:
            pass
        dpg.add_input_text(
                tag="email_item", 
                hint="Input email",
                default_value=email or "",
                pos=(window_width // 2 - 180, window_height // 2 - 90),
                width=input_field_width
            )
        dpg.add_input_text(tag="password_item",
                hint="Input password",
                default_value=password or "",
                pos=(window_width // 2 - 180, window_height // 2 - 40),
                width=input_field_width,
                password=True
            )
        dpg.add_text(default_value="Connection established!", 
                tag="connect_notice", 
                pos=(window_width // 2 - 145, window_height // 2 - 60),
                show=False
            )
        dpg.add_button(label="Connect", 
                callback=event.connect_button_clicked,
                pos=(window_width // 2 - 85, window_height // 2 + 80), 
                width=150, height=50,
                tag="connect_button"
            )
        dpg.add_button(label="Disconnect", 
                callback=event.disconnect_button_clicked,
                pos=(window_width // 2 - 100, window_height // 2 + 40), 
                width=180, height=50,
                tag="disconnect_button",
                show=False
            )
        dpg.add_checkbox(label="Remember login",
                pos=(window_width // 2 - 130, window_height // 2 + 20),
                tag="remember_checkbox"
            )
        dpg.set_exit_callback(callback=event.close_clicked)

    dpg.set_primary_window("Primary Window", True)



def start_nsuda():
    handler = event.HandlerBuilder.get_instanse()
    
    i: int = 0

    while(dpg.is_dearpygui_running()):
        dpg.render_dearpygui_frame()
        i += 1
        if i == 1000:
            handler.restart_if_needed()
            i = 0
    dpg.destroy_context()

