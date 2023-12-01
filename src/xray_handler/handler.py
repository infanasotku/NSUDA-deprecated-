import requests as r
from multiprocessing import Process
import subprocess as sproc
from pathlib import Path
import psutil
from datetime import datetime

class Handler:
    def __init__(self, email: str):
        self.email = email
        self._xray_executor: Process = None
        self._xray_config: str = None
        self._last_update: datetime = None

    def _execute(config, path):
            try:
                sproc.run(path.encode(), input=config.encode())
            except Exception as e:
                print(f"Xray have an error: {e}")

    def start(self):
        path = (Path(__file__).parent / "xray").absolute().as_posix()
        
        self._xray_executor = Process(
            group=None, kwargs={ "config": self._xray_config,
                                "path": path }, 
            target=Handler._execute,
            daemon=True)
        self._xray_executor.start()

    def kill(self):
        process = psutil.Process(self._xray_executor.pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
        self._xray_executor.join()

    def check_status(self) -> bool: 
        try:
            req = r.get("http://www.google.com", 
                proxies={ "http": "http://127.0.0.1:2081" })
            if req.status_code == 503:
                 return False
        except:
             return False
        return True

    def load_config(self):
        data = r.get(
            f"https://infanasotku.ru/get_config?email={self.email}"
            ).json()
        
        self._xray_config = data["config"]
        self._last_update = data["last_update"]