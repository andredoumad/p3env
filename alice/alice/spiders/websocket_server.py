import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import os
# import standalone_tools
# from standalone_tools import *
# from .AliceRequiredModules import *
import standalone_tools 
from standalone_tools import *
# import scrapy
# from scrapy.crawler import CrawlerProcess
# import Alice
# from Alice import Charlotte
# from standalone_tools import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        eventlog ('connection opened...')
        self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        eventlog("on_message: " + str(message))
        loaded_dict_data = standalone_tools.json.loads(message)
        spider_command = loaded_dict_data.get('spider_command', None)
        message = loaded_dict_data.get('message', None)
        robot_id = loaded_dict_data.get('robot_id', None)
        human = loaded_dict_data.get('human', None)
        username = loaded_dict_data.get('username', None)

        if spider_command == 'start_spider':
            eventlog('starting spider!')

        
        # self.write_message(
        #     {
        #     "message": str(message),
        #     "robot_id": str(robot_id),
        #     "human": str(human),
        #     "username": str(username)
        #     }
        # )

    def on_close(self):
        eventlog('connection closed...')




class WebsocketServer:

    def __init__(self):
        self.application = tornado.web.Application([
            (r'/ws', WSHandler),
            (r'/', MainHandler),
            (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
        ])
        self.application.listen(9090)
        tornado.ioloop.IOLoop.instance().start()

    # application = tornado.web.Application([
    #     (r'/ws', WSHandler),
    #     (r'/', MainHandler),
    #     (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
    # ])





if __name__ == "__main__":
    eventlog('directory: ' + str(os.getcwd()))
    # application.listen(9090)
    # tornado.ioloop.IOLoop.instance().start()
    server = WebsocketServer()

    process.crawl(MySpider)
    process.start()  # the script will block here until the crawling is finished