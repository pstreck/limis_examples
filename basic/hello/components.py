from limis.services.components import Component

from hello.handlers import HelloHTTPHandler, HelloWebSocketHandler


class HelloComponent(Component):
    component_name = 'hello'
    component_path = 'hello'
    component_http_handler = HelloHTTPHandler
    component_websocket_handler = HelloWebSocketHandler

    def hello(self):
        return 'hello'
