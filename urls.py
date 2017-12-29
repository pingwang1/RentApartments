# coding:utf-8

import os

from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from handlers import Passport, VerifyCode
    #, Profile, House, Orders

urls = [
    # (r"/log", Passport.LogHandler),
    (r"/api/register", Passport.RegisterHandler),
    (r"/(.*)", StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]

