from fastapi import FastAPI

from inject import view as inject

app = FastAPI()
app.include_router(inject.router)
