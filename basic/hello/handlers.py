from typing import Union

from tornado.websocket import WebSocketHandler
from limis.services.handlers import ComponentHandler


class HelloHTTPHandler(ComponentHandler):
    def get(self):
        self.write(self.component_class().hello())


class HelloWebSocketHandler(ComponentHandler, WebSocketHandler):
    def on_message(self, message: Union[str, bytes]):
        self.write_message(self.component_class().hello())
