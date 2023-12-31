from xray_handler.messenger import MessengerBuilder
import dearpygui.dearpygui as dpg
from threading import Thread
from config import window_width, window_height, app_folder_path, login_file_name

class UIData:
    '''Keeps the UI data.
    '''
    def __init__(self):
        self.load_screen_data = []
        self.load_end_event = False
        self.loading_process: Thread = None

class UIDataBuilder:
    '''Provides access to UIData singleton instance.
    '''
    _instance:UIData = None

    @staticmethod
    def get_instanse():
        if not UIDataBuilder._instance:
            UIDataBuilder._instance = UIData()
        return UIDataBuilder._instance

small_font = None

def show_main_menu(show: bool):
    dpg.configure_item(item="connect_button", show=show)
    dpg.configure_item(item="remember_checkbox", show=show)
    dpg.configure_item(item="email_item", show=show)
    dpg.configure_item(item="password_item", show=show)


def connect_button_clicked():
    email: str = dpg.get_value(item="email_item")
    password: str = dpg.get_value(item="password_item")
    if email == "" or password == "":
        notice_for_error("Empty strings")
        return
    if dpg.get_value(item="remember_checkbox"):
        with open(app_folder_path + "/" + login_file_name, "w") as f:
            f.write(f"{email} {password}")

    show_main_menu(show=False)
    ui_data = UIDataBuilder.get_instanse()
    ui_data.load_end_event = False
    ui_data.loading_process = Thread(daemon=True, target=view_load_screen)
    ui_data.loading_process.start()
    messenger = MessengerBuilder.get_instanse()
    msg: str = messenger.load_config(email=email, password=password)

    if msg != "OK":
        ui_data.load_end_event = True
        ui_data.loading_process.join()
        show_main_menu(show=True)
        notice_for_error(msg)
        return

    messenger.run_session()
    messenger.handle_xray()
    ui_data.load_end_event = True
    ui_data.loading_process.join()
    dpg.configure_item(item="disconnect_button", show=True)
    dpg.configure_item(item="connect_notice", show=True)

def notice_for_error(notice: str):
    with dpg.window(
        width=350, 
        height=100, 
        no_resize=True,
        label="Notice",
        pos=(window_width // 2 - 175, window_height // 2 - 90),
        no_move=True,
        no_collapse=True
        ) as notice_window:
        dpg.add_text(default_value=notice,
                     pos=(10, 47),
                     )
        dpg.bind_item_font(notice_window, small_font)

def disconnect_button_clicked():
    show_main_menu(show=True)
    dpg.configure_item(item="connect_notice", show=False)
    dpg.configure_item(item="disconnect_button", show=False)
    MessengerBuilder.get_instanse().kill()

import time

def view_load_screen():
    dpg.configure_item(item="load_screen", show=True)
    dpg.configure_item(item="connecting_notice", show=True)
    ui_data = UIDataBuilder.get_instanse()
    i = 0
    while True:
        for gif_data in ui_data.load_screen_data:
            if ui_data.load_end_event:
                dpg.configure_item(item="load_screen", show=False)
                dpg.configure_item(item="connecting_notice", show=False)
                return
            i += 1
            i %= 40
            dpg.configure_item(item="connecting_notice", 
                               default_value="Connecting" + (i // 10) * '.')
            dpg.set_value("load_screen_texture", gif_data)
            time.sleep(0.02)

def close_clicked():
    ui_data = UIDataBuilder.get_instanse()
    ui_data.load_end_event = True
    if MessengerBuilder.get_state():
        return
    messenger = MessengerBuilder.get_instanse()
    try:
        messenger.kill()
    except:
        pass


def disable_fullscreen(): 
    import win32con
    import win32gui
    import win32api
    hwnd = win32gui.GetForegroundWindow() 
    win32api.SetWindowLong(hwnd, 
                           win32con.GWL_STYLE, 
                           win32api.GetWindowLong(hwnd, 
                                                  win32con.GWL_STYLE) & ~win32con.WS_MAXIMIZEBOX)
