import sys
import subprocess as sub
import pathlib

CURRENT_DIRECTORY = pathlib.Path(__file__).parent.resolve()
EXECUTEABLE_PATH = sys.executable

def run():
    commands: list[list] = []

    # Backend
    backend_cmd = [f"{EXECUTEABLE_PATH}", f"{CURRENT_DIRECTORY}/src/backend/manage_backend.py"]
    commands.append(backend_cmd)

    # Frontend
    frontend_cmd = [f"npm", "--prefix", f"{CURRENT_DIRECTORY}/src/frontend", "run", "dev"]
    commands.append(frontend_cmd)

    if sys.argv[1] == "DEBUG":
        add_debug_args(backend_cmd=backend_cmd, frontend_cmd=frontend_cmd)
    elif sys.argv[1] == "RELEASE":
        add_release_args(backend_cmd=backend_cmd, frontend_cmd=frontend_cmd)

    procs: list[sub.Popen] = []
    for cmd in commands:
        proc = sub.Popen(args=cmd)
        procs.append(proc)

    for proc in procs:
        proc.wait()

def add_debug_args(frontend_cmd: list, backend_cmd: list):
    # TODO: add debug args
    print("Debug args confirmed")

def add_release_args(frontend_cmd: list, backend_cmd: list):
    # TODO: add release args
    print("Release args confirmed")
    
if __name__ == "__main__":
    run()

    
