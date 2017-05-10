from channels.routing import route
from ConnectAgency.consumers import ws_message, ws_connect, ws_disconnect
from channels.staticfiles import StaticFilesConsumer


channel_routing = [
    route("http.request", StaticFilesConsumer()),
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]