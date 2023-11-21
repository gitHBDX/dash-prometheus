import dash
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from . import registry

def add_middleware(app: dash.Dash, slug: str = "metrics"):
    app.server.wsgi_app = DispatcherMiddleware(app.server.wsgi_app, {f"/{slug}": make_wsgi_app(registry=registry)})
