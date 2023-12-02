import win32com.shell.shell as shell
import os
from pathlib import Path
from config import is_development
from build import WINDOWS_XRAY_FOLDER

xray_path:str = None

if is_development:
    xray_path = (Path(__file__).parent / "xray").absolute().as_posix()
else:
    xray_path = (Path(__file__).parent.parent.parent / WINDOWS_XRAY_FOLDER / "xray").absolute().as_posix()

def load_env_setting():
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v PrivacyAdvanced /t REG_DWORD /d 1 /f')
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v MigrateProxy /t REG_DWORD /d 1 /f')
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v EnableNegotiate /t REG_DWORD /d 1 /f')
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v DisableCachingOfSSLPages /t REG_DWORD /d 0 /f')
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v CertificateRevocation /t REG_DWORD /d 1 /f')
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d localhost:2081 /f')
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ r'netsh winhttp import proxy source=ie /f')

def start_env():
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f')


def exit_env():
    os.system(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')
