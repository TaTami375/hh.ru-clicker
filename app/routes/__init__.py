"""
FastAPI app creation and route registration.
"""

import base64
import hashlib
import os
import secrets
from pathlib import Path

from fastapi import FastAPI, Request, Response, WebSocket
from fastapi.staticfiles import StaticFiles

# Singleton bot/manager are created in app.instances so every router module
# can import them without pulling in the package __init__ (avoids circular imports).
from app.instances import bot, manager  # re-exported for back-compat

app = FastAPI(title="HH Bot Dashboard")

_DASHBOARD_PASSWORD = os.environ.get("DASHBOARD_PASSWORD", "")
# Токен для WebSocket-соединений: sha256(password), передаётся как ?token=...
_WS_TOKEN = hashlib.sha256(_DASHBOARD_PASSWORD.encode()).hexdigest() if _DASHBOARD_PASSWORD else ""


def _check_basic_auth(auth_header: str) -> bool:
    if not auth_header.startswith("Basic "):
        return False
    try:
        decoded = base64.b64decode(auth_header[6:]).decode("utf-8", errors="replace")
        _, _, pwd = decoded.partition(":")
        return secrets.compare_digest(pwd, _DASHBOARD_PASSWORD)
    except Exception:
        return False


@app.middleware("http")
async def basic_auth_middleware(request: Request, call_next):
    if not _DASHBOARD_PASSWORD:
        return await call_next(request)
    # WebSocket upgrade — проверяем ?token= (Basic Auth недоступен для WS в браузере)
    if request.headers.get("upgrade", "").lower() == "websocket":
        token = request.query_params.get("token", "")
        if _WS_TOKEN and secrets.compare_digest(token, _WS_TOKEN):
            return await call_next(request)
        return Response(status_code=401, content="Unauthorized")
    # Обычные HTTP-запросы — Basic Auth
    if _check_basic_auth(request.headers.get("Authorization", "")):
        return await call_next(request)
    return Response(
        status_code=401,
        headers={"WWW-Authenticate": 'Basic realm="HH Bot Dashboard"'},
        content="Unauthorized",
    )

@app.get("/api/ws_token")
async def api_ws_token():
    """Возвращает токен для WebSocket-соединения (доступен только авторизованным)."""
    return {"token": _WS_TOKEN}


STATIC_DIR = Path("static")
STATIC_DIR.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

# -- Register routers (imported after app is created) --
from app.routes.core import router as core_router          # noqa: E402
from app.routes.accounts import router as accounts_router  # noqa: E402
from app.routes.sessions import router as sessions_router  # noqa: E402
from app.routes.data import router as data_router          # noqa: E402
from app.routes.apply import router as apply_router        # noqa: E402
from app.routes.settings import router as settings_router  # noqa: E402
from app.routes.llm import router as llm_router            # noqa: E402
from app.routes.debug import router as debug_router        # noqa: E402

app.include_router(core_router)
app.include_router(accounts_router)
app.include_router(sessions_router)
app.include_router(data_router)
app.include_router(apply_router)
app.include_router(settings_router)
app.include_router(llm_router)
app.include_router(debug_router)
