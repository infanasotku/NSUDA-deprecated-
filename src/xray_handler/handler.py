import requests as r
from multiprocessing import Process
import subprocess as sproc
import psutil
from datetime import datetime
import platform
if platform.system() == "Windows":
    from xray_handler.windows import win_handler as os_handler
elif platform.system() == "Darwin":
    from xray_handler.mac_os import mac_handler as os_handler
elif platform.system() == "Linux":
    from xray_handler.linux import lin_handler as os_handler

class Handler:

    def __init__(self):
        self._is_running = False
        self._xray_executor: Process = None
        self._xray_config: str = None
        self._last_update: datetime = None
        self.email = None
        self.password = None
        self.module = os_handler
        self._load_env_setting()

    @staticmethod
    def _execute(config, path):
            try:
                sproc.run(path, 
                          input=config.encode(),
                          shell=True)
            except Exception as e:
                print(f"Xray have an error: {e}")

    def start(self):
        path = self.module.xray_path
        
        self._xray_executor = Process(
            group=None, kwargs={ "config": self._xray_config,
                                "path": path }, 
            target=Handler._execute,
            daemon=True)
        self._xray_executor.start()
        self._is_running = True
        self.module.start_env()


    def kill(self):
        process = psutil.Process(self._xray_executor.pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
        self._xray_executor.join()
        self.module.exit_env()
        self._is_running = False


    def check_status(self) -> bool: 
        try:
            req = r.get("http://www.google.com", 
                proxies={ "http": "http://127.0.0.1:2081" })
            if req.status_code == 503:
                 return False
        except:
             return False
        return True

    def load_config(self, email: str, password: str) -> str:
        self.email = email
        self.password = password
        try:
            data = r.get(
                f"https://infanasotku.ru/get_config?email={email}&password={password}"
                ).json()
        except:
            return "Undefined error"
        if "error" in data:
            return data["error"]
        self._xray_config = data["config"]
        self._last_update = data["last_update"]
        return "OK"

    def restart_if_needed(self):
        if self._is_running:
            is_alive = self.check_status()
            if not is_alive:
                self.kill()
                try:
                    self.load_config(email=self.email, password=self.password)
                    self.start()
                    return
                except:
                    pass
            



    def _load_env_setting(self):
        self.module.load_env_setting()
