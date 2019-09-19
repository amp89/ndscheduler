


from ndscheduler import settings
import time


def is_auth(u,p):
    """
    Customize auth here
    """
    assert u
    assert p
    u = u.strip().lower()
    p = p.strip().lower()
    assert u
    assert p
    if u and p and u in settings.ALLOWED_USERNAME_LIST:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        do auth here, this is not auth, this is stupid nonsense to make the cookies work for testing
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        assert settings.TMP_LOCALHOST_P
        if p == settings.TMP_LOCALHOST_P:
            return True
        else:
            return False
    else:
        return False

def create_cookie_data(u, create_ts=None):
    u = u.strip().lower()
    assert u
    assert settings.COOKIE_KEY
    if not create_ts:
        create_ts = int(time.time())
    lu_ts = int(time.time())
    cookie_str = f"ck_{u}_{create_ts}_{settings.COOKIE_KEY}_{lu_ts}"
    return cookie_str

def check_and_get_update_cookie_and_get_user(cookie):
    '''returns new_cookie, user, authenticated_book
    '''
    
    try:
        cookie = cookie.strip().lower()
        assert cookie
        assert settings.COOKIE_KEY
        cookie_crumbs = cookie.split("_")
        assert str(settings.COOKIE_KEY).strip().lower() == str(cookie_crumbs[3]).strip().lower()
        
        create_ts = int(cookie_crumbs[2].strip().strip("\'").strip("\""))
        lu_ts = int(cookie_crumbs[4].strip().strip("\'").strip("\""))
        now_ts = int(time.time())
        assert create_ts + settings.COOKIE_TIMEOUT_SECONDS >= now_ts
        assert lu_ts + settings.STALE_COOKIE_TIMEOUT_SECONDS >= now_ts

        user = cookie_crumbs[2]

        cookie_str = create_cookie_data(u=user, create_ts=create_ts)
            
        return cookie_str, user, True
    except AssertionError as e:
        return None, None, False




