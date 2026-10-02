from typing import Annotated
from fastapi import FastAPI, Depends
import uvicorn
from router import router as task_router

from contextlib import asynccontextmanager
from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("База очищена")

    await create_tables()
    print("База готова к работе")

    yield

    # Clean up the ML models and release the resources
    print("Выключение")
    

app = FastAPI(lifespan=lifespan)

app.include_router(task_router)














if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 