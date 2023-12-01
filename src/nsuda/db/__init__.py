from nsuda.db.database import engine, isDataBaseInited
from nsuda.db import models

if not isDataBaseInited:
    try:
        models.Base.metadata.create_all(bind=engine)
        print("Database initialized successfully")
        isDataBaseInited = True
    except:
        print("Database initialized error")

