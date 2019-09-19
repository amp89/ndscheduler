"""Base tornado.web.RequestHandler classes.

This package provides a common set of RequestHandler objects to be
subclassed in the rest of the app for different URLs.
"""

import json

from concurrent import futures

import tornado.ioloop
import tornado.web

from ndscheduler import settings
from ndscheduler.auth_utils.cookie_monster import check_and_get_update_cookie_and_get_user

'''
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set yet!")
        else:
            self.write("Your cookie was set!")

            need to put cookie_secret in where 
            
            application = tornado.web.Application([
    (r"/", MainHandler),
], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

'''

class BaseHandler(tornado.web.RequestHandler):

    executor = futures.ThreadPoolExecutor(max_workers=settings.TORNADO_MAX_WORKERS)

    def prepare(self):
        """Preprocess requests."""
        auth_cookie_raw = self.get_secure_cookie(settings.ND_LOGON_TOKEN_NAME)
        if not auth_cookie_raw:
            self.redirect("/login/")
        auth_cookie = str(auth_cookie_raw)
        # self.set_secure_cookie("mycookie", "stuff")
        
        new_cookie_str, user, authenticated = check_and_get_update_cookie_and_get_user(cookie=auth_cookie)
        if authenticated:
            print("is authenticated....")
            self.set_secure_cookie(settings.ND_LOGON_TOKEN_NAME, new_cookie_str)
            print("reset_cookie....")
        else:
            print("redirecting to login")
            self.redirect("/login/")
        
        try:
            if self.request.headers['Content-Type'].startswith('application/json'):
                self.json_args = json.loads(self.request.body.decode())
        except KeyError:
            self.json_args = None
        print("yayyyyyyyyyyyy")
        # For audit log
        self.username = user
        self.scheduler_manager = self.application.settings['scheduler_manager']
        self.datastore = self.scheduler_manager.get_datastore()

class OpenHandler(tornado.web.RequestHandler):

    executor = futures.ThreadPoolExecutor(max_workers=settings.TORNADO_MAX_WORKERS)

    def prepare(self):
        try:
            if self.request.headers['Content-Type'].startswith('application/json'):
                self.json_args = json.loads(self.request.body.decode())
        except KeyError:
            self.json_args = None

        # For audit log
        self.username = "UNAUTHENTICATED"
        self.scheduler_manager = self.application.settings['scheduler_manager']
        self.datastore = self.scheduler_manager.get_datastore()

