"""Serves the single page app web ui."""

import json

from ndscheduler import settings
from ndscheduler import utils
from ndscheduler.server.handlers import base
from ndscheduler.auth_utils.cookie_monster import is_auth
from ndscheduler.auth_utils.cookie_monster import create_cookie_data



class LoginHandler(base.OpenHandler):

    def get(self):
        self.render(settings.AUTH_PAGE)

    def post(self):

        u = self.get_body_argument("u", default=None, strip=False)
        p = self.get_body_argument("p", default=None, strip=False)
        is_authenticated = is_auth(u,p)
        del p
        if is_authenticated == True:
            cookie = create_cookie_data(u=u)
            self.set_secure_cookie(settings.ND_LOGON_TOKEN_NAME,cookie)
            self.redirect("/")
        else:
            self.clear_cookie(settings.ND_LOGON_TOKEN_NAME)
            self.redirect("/login/")

class LogoutHandler(base.OpenHandler):
    def get(self):
        self.clear_cookie(settings.ND_LOGON_TOKEN_NAME)
        self.render(settings.AUTH_PAGE)

