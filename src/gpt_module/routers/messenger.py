from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse

from pathlib import Path
srcPath = Path(__file__).parent.parent.parent.absolute()

templates = Jinja2Templates(directory=srcPath / "templates")

router = APIRouter()

import g4f

@router.get("/")
async def greet(request: Request, msg=None, response_class=PlainTextResponse):
    if not msg:
        return templates.TemplateResponse("gpt.html", { "request": request })
    else:
        res = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_4,
            provider=g4f.Provider.ChatBase,
            messages=[{"role": "user", "content": msg}],
        )
        lines = res.split('\n')
        return templates.TemplateResponse("gpt_answer.html", { "request": request, "lines": lines })