import socket
from flareworks import FlareWork
from flareworks.globals import Request

class CORS:
    def __init__(self, fl_app:FlareWork = None):
        self.app = fl_app
        if self.app is not None:
            self.decorator()

    def init_app(self, fl_app:FlareWork):
        self.app = fl_app
        self.decorator()

    def decorator(self):
        @self.app.before_request
        def ensure_cors(request:Request):
            if request.remote.addr == "127.0.0.1" or request.remote.addr == socket.gethostbyname(socket.gethostname()):
                return True

            return False
