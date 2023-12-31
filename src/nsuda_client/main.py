import dearpygui.dearpygui as dpg
import nsuda_client.event as event
import platform

from config import *


def configure_load_screen():
    ui_data = event.UIDataBuilder.get_instanse()
    gif_width = None
    gif_height = None
    for i in range(1, 35):
        gif_width, gif_height, _, gif_data = dpg.load_image(resource_path + f"/gif/flying-{i}.png")
        ui_data.load_screen_data.append(gif_data)

    with dpg.texture_registry(show=False):
        gif_data = ui_data.load_screen_data[0]
        dpg.add_dynamic_texture(width=gif_width,
                                height=gif_height,
                                    default_value=gif_data,
                                    tag="load_screen_texture")

def configure_nsuda():
    configure_load_screen()
    with dpg.font_registry():
        default_font = dpg.add_font(resource_path + "/Gill Sans.ttf", 30)
        event.small_font = dpg.add_font(resource_path + "/Gill Sans.ttf", 21)
        dpg.bind_font(default_font)
    with dpg.window(tag="Primary Window"):
        email, password = None, None
        try:
            with open(app_folder_path + "/" + login_file_name, "r") as f:
                email, password = f.read().split()
        except:
            pass

        dpg.add_input_text(
                tag="email_item", 
                hint="Input email",
                default_value=email or "",
                pos=(window_width // 2 - 175 + width_shift, 
                     window_height // 2 - 90 + height_shift),
                width=input_field_width
            )
        dpg.add_input_text(tag="password_item",
                hint="Input password",
                default_value=password or "",
                pos=(window_width // 2 - 175 + width_shift, 
                     window_height // 2 - 40 + height_shift),
                width=input_field_width,
                password=True
            )
        dpg.add_text(default_value="Connection established!", 
                tag="connect_notice", 
                pos=(window_width // 2 - 140 + width_shift, 
                     window_height // 2 - 60 + height_shift),
                show=False
            )
        dpg.add_button(label="Connect", 
                callback=event.connect_button_clicked,
                pos=(window_width // 2 - 82 + width_shift, 
                     window_height // 2 + 80 + height_shift), 
                width=150, height=50,
                tag="connect_button"
            )
        dpg.add_button(label="Disconnect", 
                callback=event.disconnect_button_clicked,
                pos=(window_width // 2 - 92 + width_shift, 
                     window_height // 2 + 40 + height_shift), 
                width=180, height=50,
                tag="disconnect_button",
                show=False
            )
        dpg.add_checkbox(label="Remember me",
                pos=(window_width // 2 - 114 + width_shift, 
                     window_height // 2 + 20 + height_shift),
                tag="remember_checkbox"
            )
        dpg.set_exit_callback(callback=event.close_clicked)
        dpg.add_image(texture_tag="load_screen_texture",
                      tag="load_screen",
                      show=False,
                      pos=(window_width // 2 - 101 + width_shift, 
                           window_height // 2 - 120 + height_shift))
        dpg.add_text(default_value="Connecting", 
                tag="connecting_notice", 
                pos=(window_width // 2 - 70 + width_shift, 
                     window_height // 2 + 85 + height_shift),
                show=False
            )

    dpg.set_primary_window("Primary Window", True)
from xray_handler.messenger import MessengerBuilder
from nsuda_client.win import disable_fullscreen

def start_nsuda():
    MessengerBuilder.get_instanse()
    if platform.system() == "Windows":
        dpg.render_dearpygui_frame()
        disable_fullscreen()
    while(dpg.is_dearpygui_running()):
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

