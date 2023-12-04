import PyInstaller.__main__
import platform

RESOURCE_FOLDER: str = "resource"
XRAY_FOLDER: str = None

BUILDER_ARGS: list = [
    'run.py',
    '--noconfirm',
    '--onefile',
    '--name=NSUDA',
    '--noconsole',
    '--add-data=nsuda_client/resource/Logo.ico:' + RESOURCE_FOLDER,
    '--add-data=nsuda_client/resource/Logo.png:' + RESOURCE_FOLDER,
    '--add-data=nsuda_client/resource/Gill Sans.ttf:' + RESOURCE_FOLDER,
]

icon_name: str = None

if platform.system() == "Windows":
    XRAY_FOLDER = "windows"
    icon_name = "Logo.ico"
    BUILDER_ARGS.append(
        '--add-data=xray_handler/windows/*.dat:' + XRAY_FOLDER,
    )
    BUILDER_ARGS.append(
        '--add-data=xray_handler/windows/xray.exe:' + XRAY_FOLDER,
    )
elif platform.system() == "Darwin":
    XRAY_FOLDER = "mac_os"
    icon_name = "Logo.png"
    arch_folder: str = platform.uname().machine
    BUILDER_ARGS.append(
        '--add-data=xray_handler/mac_os/' + arch_folder + '/*.dat:' + XRAY_FOLDER,
    )
    BUILDER_ARGS.append(
        '--add-data=xray_handler/mac_os/' + arch_folder + '/xray:' + XRAY_FOLDER,
    )
BUILDER_ARGS.append(
    '--icon=nsuda_client/resource/' + icon_name
)


if __name__ == "__main__":
    PyInstaller.__main__.run(BUILDER_ARGS)