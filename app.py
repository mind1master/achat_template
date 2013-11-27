import cyclone.escape
import cyclone.web
import cyclone.websocket
import os.path
import sys
from twisted.python import log
from twisted.internet import reactor

class Application(cyclone.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        handlers = [
            (r"/", MainHandler),
        ]
        cyclone.web.Application.__init__(self, handlers, **settings)


class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.render("base.html")

def main():
    reactor.listenTCP(8888, Application())
    reactor.run()


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    main()