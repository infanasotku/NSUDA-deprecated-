from xray_handler.handler import Handler
import dearpygui.dearpygui as dpg

class HandlerBuilder:
    _instanse: Handler = None

    @staticmethod
    def get_instanse() -> Handler:
        if not HandlerBuilder._instanse:
            HandlerBuilder._instanse = Handler()
        return HandlerBuilder._instanse


def connect_button_clicked():
    email: str = dpg.get_value(item="connect_item")
    dpg.configure_item(item="connect_button", show=False)
    dpg.configure_item(item="connect_item", show=False)
    dpg.configure_item(item="disconnect_button", show=True)
    handler = HandlerBuilder.get_instanse()
    handler.load_config(email)
    handler.start()
    

def disconnect_button_clicked():
    dpg.configure_item(item="connect_button", show=True)
    dpg.configure_item(item="connect_item", show=True)
    dpg.configure_item(item="disconnect_button", show=False)
    handler = HandlerBuilder.get_instanse()
    handler.kill()
