import inspect
import time
from functools import wraps

import dash
from prometheus_client import Counter, Histogram

from . import registry

_unpatched_dash_dot_callback = dash.callback

counter = Counter("dash_callback_calls", "Number of calls to Dash callback", ["file", "callback"], registry=registry)
histogram = Histogram(
    "dash_callback_duration",
    "Duration of Dash callback",
    ["file", "callback"],
    buckets=(0.001, 0.01, 0.1, 1, 5, 10, 30, 60, 120, 300),
    registry=registry,
)


def dash_callback_overwrite(*args, **kwargs):
    dash_wrapper = _unpatched_dash_dot_callback(*args, **kwargs)

    def wrapper(func):
        # module = inspect.getmodule(func).__spec__.name
        file = inspect.getfile(func)
        callback = func.__name__

        @wraps(func)
        def wrapped(*args, **kwargs):
            start_time = time.perf_counter()

            results = func(*args, **kwargs)

            end_time = time.perf_counter()
            counter.labels(file, callback).inc()
            histogram.labels(file, callback).observe(end_time - start_time)

            return results

        return dash_wrapper(wrapped)

    return wrapper


dash.callback = dash_callback_overwrite
