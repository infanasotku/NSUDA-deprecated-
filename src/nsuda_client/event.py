from xray_handler.handler import Handler
import dearpygui.dearpygui as dpg
from config import window_width, window_height

small_font = None

class HandlerBuilder:
    _instanse: Handler = None

    @staticmethod
    def get_instanse() -> Handler:
        if not HandlerBuilder._instanse:
            HandlerBuilder._instanse = Handler()
        return HandlerBuilder._instanse
    
    @staticmethod
    def get_state() -> bool:
        return HandlerBuilder._instanse == None


def connect_button_clicked():
    email: str = dpg.get_value(item="email_item")
    password: str = dpg.get_value(item="password_item")
    handler = HandlerBuilder.get_instanse()
    msg: str = handler.load_config(email=email, password=password)
    if msg != "OK":
        notice_for_error(msg)
        return
    dpg.configure_item(item="connect_button", show=False)
    dpg.configure_item(item="email_item", show=False)
    dpg.configure_item(item="password_item", show=False)
    dpg.configure_item(item="disconnect_button", show=True)
    dpg.configure_item(item="connect_notice", show=True)
    handler.start()
    
def notice_for_error(notice: str):
    with dpg.window(
        width=350, 
        height=100, 
        no_resize=True,
        label="Notice",
        pos=(window_width // 2 - 180, window_height // 2 - 80),
        no_move=True,
        no_collapse=True
        ) as notice_window:
        text = dpg.add_text(default_value=notice,
                     pos=(10, 47),
                     )
        dpg.bind_item_font(notice_window, small_font)

def disconnect_button_clicked():
    dpg.configure_item(item="connect_button", show=True)
    dpg.configure_item(item="email_item", show=True)
    dpg.configure_item(item="password_item", show=True)
    dpg.configure_item(item="connect_notice", show=False)
    dpg.configure_item(item="disconnect_button", show=False)
    handler = HandlerBuilder.get_instanse()
    handler.kill()

def close_clicked():
    if HandlerBuilder.get_state():
        return
    handler = HandlerBuilder.get_instanse()
    try:
        handler.close_handler()
    except:
        pass