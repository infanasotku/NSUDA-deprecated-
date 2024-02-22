def run_backend():
    import uvicorn
    from core.app import app
    uvicorn.run(app=app, host='localhost', port=5000)

if __name__ == "__main__":
    run_backend()