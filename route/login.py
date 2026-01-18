from fastapi import Request, HTTPException, APIRouter
from fastapi.responses import RedirectResponse
from auth import oauth

router = APIRouter()

@router.get("/login")
async def login(request: Request):
    uri = request.url_for('login_callback')
    return await oauth.google.authorize_redirect(request, uri)

@router.get("/callback")
async def login_callback(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except:
        raise HTTPException(status_code=401, detail="Failed to login")

    user = token.get('userinfo')
    if user:
        print(user)
        request.session["user"] = dict(user)
        print(token.get("email"))

    return RedirectResponse("/", status_code=301)

@router.get("/logout")
async def logout(request: Request):
    if "user" in request.session:
        request.session.pop("user")
        return {"result": True, "message": "Logged out"}

    return {"result": False, "message": "There is no sessions"}