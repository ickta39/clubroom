from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/user/{id}")
async def self_info(request: Request, id: str):
    if id != "me": return "??"

    if not "user" in request.session:
        pass

    session = request.session["user"]

    return {
        "logged_in": True,
        "session": dict(session)
    }