import requests as r
from multiprocessing import Process
import subprocess as sproc
from pathlib import Path
import psutil
from datetime import datetime
import os
import win32com.shell.shell as shell


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
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f')

    def kill(self):
        process = psutil.Process(self._xray_executor.pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
        self._xray_executor.join()
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')

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

    def load_env_setting(self):
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v PrivacyAdvanced /t REG_DWORD /d 1 /f')
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v MigrateProxy /t REG_DWORD /d 1 /f')
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v EnableNegotiate /t REG_DWORD /d 1 /f')
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v DisableCachingOfSSLPages /t REG_DWORD /d 0 /f')
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v CertificateRevocation /t REG_DWORD /d 1 /f')
        os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d localhost:2081 /f')
        self._run_as_admin(r'netsh winhttp import proxy source=ie /f')

    def _run_as_admin(self, command: str):
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ command)