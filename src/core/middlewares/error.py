from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response, HTMLResponse

class HttpErrorMiddleware(BaseHTTPMiddleware):
    
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        
        if response.status_code < 400:
            return response
        elif response.status_code == 404:
            return self.error_404()
        elif response.status_code == 500:
            return self.error_500()
    
        

    def error_404(self) -> Response:
        return HTMLResponse(content="""
    <h1>404</h1>
""", status_code=404)
    
    def error_500(self) -> Response:
        return HTMLResponse(content="""
    <h1>500</h1>
""", status_code=500)


