import PyInstaller.__main__


WINDOWS_XRAY_FOLDER = "windows"
RESOURCE_FOLDER = "resource"

if __name__ == "__main__":
    PyInstaller.__main__.run([
        'run.py',
        '--add-data=xray_handler/windows/*.dat:' + WINDOWS_XRAY_FOLDER,
        '--add-data=xray_handler/windows/xray.exe:' + WINDOWS_XRAY_FOLDER,
        '--add-data=xray_handler/windows/xray.exe:' + WINDOWS_XRAY_FOLDER,
        '--add-data=nsuda_client/resource/Logo.ico:' + RESOURCE_FOLDER,
        '--add-data=nsuda_client/resource/Logo.png:' + RESOURCE_FOLDER,
        '--icon=nsuda_client/resource/Logo.ico',
        '--noconfirm',
        '--onefile',
        '--name=NSUDA',
        '--noconsole'
    ])