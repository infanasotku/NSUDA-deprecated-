import uvicorn
from core.app import app

def run_backend():
    uvicorn.run(app=app, host='localhost', port=5000)


def run_view():
    pass



if __name__ == "__main__":
    run_backend()
    run_view()