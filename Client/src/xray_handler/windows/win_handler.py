import win32com.shell.shell as shell
import os
from pathlib import Path
from config import is_development
from build import XRAY_FOLDER
import subprocess

xray_path:str = None
CREATE_NO_WINDOW = 0x08000000

if is_development:
    xray_path = (Path(__file__).parent / "xray").absolute().as_posix()
else:
    xray_path = (Path(__file__).parent.parent.parent / XRAY_FOLDER / "xray").absolute().as_posix()

def load_env_setting():
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v PrivacyAdvanced /t REG_DWORD /d 1 /f', creationflags=CREATE_NO_WINDOW)
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v MigrateProxy /t REG_DWORD /d 1 /f', creationflags=CREATE_NO_WINDOW)
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v EnableNegotiate /t REG_DWORD /d 1 /f', creationflags=CREATE_NO_WINDOW)
    
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v DisableCachingOfSSLPages /t REG_DWORD /d 0 /f', creationflags=CREATE_NO_WINDOW)
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v CertificateRevocation /t REG_DWORD /d 1 /f', creationflags=CREATE_NO_WINDOW)
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d localhost:2081 /f', creationflags=CREATE_NO_WINDOW)
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f', creationflags=CREATE_NO_WINDOW)

    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ r'netsh winhttp import proxy source=ie /f')

def start_env():
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f', creationflags=CREATE_NO_WINDOW)


def exit_env():
    subprocess.call(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f', creationflags=CREATE_NO_WINDOW)
