#coding:utf-8
#启动Web APP 时使用这个文件

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import torndb
import config
import redis

from handlers import Passport
from urls import urls
from tornado.options import options,define
from tornado.web import RequestHandler

define("port",default=7000,type=int,help="run server on the given port.")

class Application(RequestHandler):
	def __init__(self,*args,**kwargs):
		super(Application,self).__init__(*args,**kwargs)
		self.db = torndb.Connection(**config.mysql_options)
		self.redis=redis.StrictRedis(**config.redis_options)

def main():
	options.log_file_prefix = config.log_path
	options.loggin = config.log_level
	tornado.options.parse_command_line()
	app = Application(
		urls,
		**config.settings
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port,address="0.0.0.0")
	tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
	main()