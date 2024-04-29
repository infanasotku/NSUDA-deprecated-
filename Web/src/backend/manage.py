from core.main import create
from settings import get_settings
import uvicorn


def run():
    uvicorn.run(
        app=create(),
        host=get_settings().host,
        port=get_settings().port
    )


if __name__ == "__main__":
    run()
