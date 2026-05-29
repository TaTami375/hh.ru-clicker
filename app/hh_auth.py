"""
Auto-login to hh.ru via POST request — obtains fresh cookies from credentials.
"""

import re
import requests

from app.logging_utils import log_debug
from app.config import SSL_VERIFY

_LOGIN_URL = "https://hh.ru/account/login"
_XSRF_URL = "https://hh.ru/"

_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

_AUTH_COOKIE_KEYS = {
    "hhtoken", "_xsrf", "hhul", "crypted_id", "iap.uid",
    "hhrole", "regions", "GMT", "hhuid", "crypted_hhuid",
}


def login_and_get_cookies(login: str, password: str) -> dict | None:
    """
    Perform a headless login to hh.ru using login/password.

    Returns a dict of auth cookies on success, or None on failure.
    The returned dict includes at minimum: hhtoken, _xsrf.
    """
    if not login or not password:
        log_debug("hh_auth: login or password is empty")
        return None

    session = requests.Session()
    session.headers.update({"User-Agent": _UA})

    # ── Step 1: GET hh.ru to obtain initial _xsrf cookie ──
    try:
        r0 = session.get(
            _XSRF_URL,
            verify=SSL_VERIFY,
            timeout=15,
            allow_redirects=True,
        )
        xsrf = session.cookies.get("_xsrf", "")
        if not xsrf:
            # Try to find xsrf in Set-Cookie headers
            for v in r0.headers.get("set-cookie", "").split(";"):
                m = re.search(r"_xsrf=([^;,\s]+)", v)
                if m:
                    xsrf = m.group(1)
                    break
        log_debug(f"hh_auth: GET / status={r0.status_code}, _xsrf={'yes' if xsrf else 'no'}")
    except Exception as e:
        log_debug(f"hh_auth: GET / error: {e}")
        return None

    # ── Step 2: GET login page to pick up any additional cookies ──
    try:
        r1 = session.get(
            _LOGIN_URL,
            params={"backUrl": "https://hh.ru/"},
            verify=SSL_VERIFY,
            timeout=15,
            allow_redirects=True,
        )
        # Refresh xsrf after login page
        fresh_xsrf = session.cookies.get("_xsrf", xsrf)
        if fresh_xsrf:
            xsrf = fresh_xsrf
        log_debug(f"hh_auth: GET login status={r1.status_code}")
    except Exception as e:
        log_debug(f"hh_auth: GET login error: {e}")
        # Continue without — xsrf from step 1 may be enough

    # ── Step 3: POST credentials ──
    payload = {
        "backUrl": "https://hh.ru/",
        "username": login,
        "password": password,
        "remember": "yes",
        "action": "login",
    }
    if xsrf:
        payload["_xsrf"] = xsrf

    try:
        r2 = session.post(
            _LOGIN_URL,
            data=payload,
            headers={
                "Referer": _LOGIN_URL,
                "Origin": "https://hh.ru",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            verify=SSL_VERIFY,
            timeout=15,
            allow_redirects=True,
        )
        log_debug(f"hh_auth: POST login status={r2.status_code}, url={r2.url}")
    except Exception as e:
        log_debug(f"hh_auth: POST login error: {e}")
        return None

    # ── Step 4: Validate result ──
    cookies = dict(session.cookies)

    # Check for captcha / error markers in response HTML
    text_lower = r2.text.lower() if r2.text else ""
    if "captcha" in text_lower or "капча" in text_lower:
        log_debug("hh_auth: captcha required — cannot auto-login")
        return None

    # Detect if we're still on the login page (failed auth)
    still_login = (
        '"/account/login"' in r2.text
        or "hh.ru/account/login" in r2.url
        or "Войти в аккаунт" in r2.text
        or '"accountLogin"' in r2.text
    ) and "hhtoken" not in cookies

    if still_login:
        log_debug("hh_auth: still on login page — wrong credentials or blocked")
        return None

    if "hhtoken" not in cookies:
        log_debug(f"hh_auth: no hhtoken in cookies after login. cookies={list(cookies.keys())}")
        return None

    auth_cookies = {k: v for k, v in cookies.items() if k in _AUTH_COOKIE_KEYS}
    log_debug(f"hh_auth: login OK for {login!r}, cookies={list(auth_cookies.keys())}")
    return auth_cookies
