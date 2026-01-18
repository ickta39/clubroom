from fastapi import FastAPI, staticfiles, Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware
import dotenv, uvicorn, os

dotenv.load_dotenv()

from route import login, user

app = FastAPI()

app.include_router(login.router, prefix="/api", tags=["auth"])
app.include_router(user.router, prefix="/api", tags=["user"])

app.mount("/", staticfiles.StaticFiles(directory="static", html=True), name="static")

app.add_middleware(SessionMiddleware, secret_key=os.getenv("GOOGLE_CLIENT_SECRET"))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="debug")