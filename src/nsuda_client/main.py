import dearpygui.dearpygui as dpg
import nsuda_client.event as event
import platform

from config import *


def disable_cb(): 
    import win32con
    import win32gui
    import win32api
    hwnd = win32gui.GetForegroundWindow() 
    win32api.SetWindowLong(hwnd, 
                           win32con.GWL_STYLE, 
                           win32api.GetWindowLong(hwnd, 
                                                  win32con.GWL_STYLE) & ~win32con.WS_MAXIMIZEBOX)

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
    if platform.system() == "Windows":
        disable_cb()
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
                pos=(window_width // 2 - 175, window_height // 2 - 90),
                width=input_field_width
            )
        dpg.add_input_text(tag="password_item",
                hint="Input password",
                default_value=password or "",
                pos=(window_width // 2 - 175, window_height // 2 - 40),
                width=input_field_width,
                password=True
            )
        dpg.add_text(default_value="Connection established!", 
                tag="connect_notice", 
                pos=(window_width // 2 - 140, window_height // 2 - 60),
                show=False
            )
        dpg.add_button(label="Connect", 
                callback=event.connect_button_clicked,
                pos=(window_width // 2 - 82, window_height // 2 + 80), 
                width=150, height=50,
                tag="connect_button"
            )
        dpg.add_button(label="Disconnect", 
                callback=event.disconnect_button_clicked,
                pos=(window_width // 2 - 92, window_height // 2 + 40), 
                width=180, height=50,
                tag="disconnect_button",
                show=False
            )
        dpg.add_checkbox(label="Remember me",
                pos=(window_width // 2 - 114, window_height // 2 + 20),
                tag="remember_checkbox"
            )
        dpg.set_exit_callback(callback=event.close_clicked)
        dpg.add_image(texture_tag="load_screen_texture",
                      tag="load_screen",
                      show=False,
                      pos=(window_width // 2 - 101, window_height // 2 - 120))
        dpg.add_text(default_value="Connecting", 
                tag="connecting_notice", 
                pos=(window_width // 2 - 70, window_height // 2 + 85),
                show=False
            )

    dpg.set_primary_window("Primary Window", True)
from xray_handler.messenger import MessengerBuilder

def start_nsuda():
    MessengerBuilder.get_instanse()
    while(dpg.is_dearpygui_running()):
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

