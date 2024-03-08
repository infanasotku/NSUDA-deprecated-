import requests as r
from threading import Thread
import subprocess
import psutil
import time
import platform
if platform.system() == "Windows":
    from xray_handler.windows import win_handler as os_handler
elif platform.system() == "Darwin":
    from xray_handler.mac_os import mac_handler as os_handler
elif platform.system() == "Linux":
    from xray_handler.linux import lin_handler as os_handler

class Messenger:

    def __init__(self):
        self._xray_process = None
        self.email: str = None
        self._xray_config: str = None
        self.on_error_event = None
        self.password: str = None
        self.is_running: bool = False
        os_handler.load_env_setting()

    def load_config(self, email: str, password: str) -> str:
        '''Gets config from API by email and password.
        '''
        if not self.check_internet_conection():
            return "Internet connection lost"
        self.email = email
        self.password = password
        try:
            data = r.get(
                f"https://infanasotku.ru/get_config?email={email}&password={password}"
                ).json()
        except Exception as e:
            print(e)
            return "Undefined error"
        if "error" in data:
            return data["error"]
        self._xray_config = data["config"]
        return "OK"

    def run_session(self) -> str:
        '''Runs xray.
        '''
        if not self._xray_config:
            return "Undefined error"
        args = [os_handler.xray_path]
        if platform.system() == "Windows":
            self._xray_process = subprocess.Popen(args=args, 
                                                  universal_newlines=True, 
                                                  stdin=subprocess.PIPE, 
                                                  stdout=subprocess.PIPE, 
                                                  creationflags=os_handler.CREATE_NO_WINDOW)
        else:
            self._xray_process = subprocess.Popen(args=args, 
                                                  universal_newlines=True, 
                                                  stdin=subprocess.PIPE, 
                                                  stdout=subprocess.PIPE)
        self._xray_process.stdin.write(self._xray_config)
        self._xray_process.stdin.close()
        os_handler.start_env()
        self.is_running = True
        return "OK"

    def _communicate(self):
        '''Returns iterator for getting xray log.
        '''
        for line in iter(self._xray_process.stdout.readline, ""):
            yield line.strip("\n")

    def kill(self):
        '''Immediately stops xray. 
        '''
        try:
            process = psutil.Process(self._xray_process.pid)
            for proc in process.children(recursive=True):
                proc.kill()
            process.kill()
            self._xray_process.stdout.close()
            self._xray_process.wait()
        except:
            pass
        finally:
            os_handler.exit_env()
            self.is_running = False

    def handle_xray(self):
        '''Handles xray process. \n
        Restarts or turns off xray if needed.\n
        '''
        logger = Thread(target=self._start_logging, daemon=True)
        handler = Thread(target=self._start_handle, daemon=True)
        handler.start()
        logger.start()
    
    def _start_logging(self):
        '''Executes handle_xray work.\n
        Logging part.
        '''
        for line in self._communicate():
            #time.sleep(5)
            # print(line)
            pass
    # TODO: Logging.
    
    def _start_handle(self):
        '''Executes handle_xray work. \n
        Handling part.
        '''
        while True:
            time.sleep(5)
            if self.is_running:
                if not self.check_xray_conection():
                    self.kill()
                    status = self.load_config(email=self.email, password=self.password)
                    if status != "OK":
                        if self.on_error_event:
                            self.on_error_event(status)
                        return
                    self.run_session()
                    self.handle_xray()
                    return
            else:
                return


    def check_xray_conection(self) -> bool:
        '''Returns True if connection with xray is stable, False otherwise.
        '''
        try:
            req = r.get("http://infanasotku.ru/", 
                proxies={ "http": "http://127.0.0.1:2081" })
            if req.status_code == 503:
                return False
        except:
                return False
        return True
    
    def check_internet_conection(self) -> bool:
        '''Returns True if connection with internet is stable, False otherwise
        '''
        try:
            req = r.get("http://infanasotku.ru/")
            if req.status_code == 503:
                return False
        except:
                return False
        return True


class MessengerBuilder:
    _instanse: Messenger = None

    @staticmethod
    def get_instanse() -> Messenger:
        if not MessengerBuilder._instanse:
            MessengerBuilder._instanse = Messenger()
        return MessengerBuilder._instanse
    
    @staticmethod
    def get_state() -> bool:
        return MessengerBuilder._instanse == None