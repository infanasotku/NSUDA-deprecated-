from xray_handler.messenger import MessengerBuilder
import dearpygui.dearpygui as dpg
from config import window_width, window_height

small_font = None

def connect_button_clicked():
    email: str = dpg.get_value(item="email_item")
    password: str = dpg.get_value(item="password_item")
    if email == "" or password == "":
        notice_for_error("Empty strings")
        return
    if dpg.get_value(item="remember_checkbox"):
        with open("login", "w") as f:
            f.write(f"{email} {password}")
    messenger = MessengerBuilder.get_instanse()
    msg: str = messenger.load_config(email=email, password=password)
    if msg != "OK":
        notice_for_error(msg)
        return
    dpg.configure_item(item="connect_button", show=False)
    dpg.configure_item(item="remember_checkbox", show=False)
    dpg.configure_item(item="email_item", show=False)
    dpg.configure_item(item="password_item", show=False)
    dpg.configure_item(item="disconnect_button", show=True)
    dpg.configure_item(item="connect_notice", show=True)
    messenger.run_session()
    messenger.handle_xray()
    
def notice_for_error(notice: str):
    with dpg.window(
        width=350, 
        height=100, 
        no_resize=True,
        label="Notice",
        pos=(window_width // 2 - 180, window_height // 2 - 90),
        no_move=True,
        no_collapse=True
        ) as notice_window:
        dpg.add_text(default_value=notice,
                     pos=(10, 47),
                     )
        dpg.bind_item_font(notice_window, small_font)

def disconnect_button_clicked():
    dpg.configure_item(item="connect_button", show=True)
    dpg.configure_item(item="email_item", show=True)
    dpg.configure_item(item="password_item", show=True)
    dpg.configure_item(item="connect_notice", show=False)
    dpg.configure_item(item="disconnect_button", show=False)
    dpg.configure_item(item="remember_checkbox", show=True)
    MessengerBuilder.get_instanse().kill()
    

def close_clicked():
    if MessengerBuilder.get_state():
        return
    messenger = MessengerBuilder.get_instanse()
    try:
        messenger.kill()
    except:
        pass