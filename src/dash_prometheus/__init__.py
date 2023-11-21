import os
import sys
import shutil
import uuid


if "dash" in sys.modules:
    raise RuntimeError("dash_prometheus must be imported before dash")


if "PROMETHEUS_MULTIPROC_DIR" in os.environ:
    prometheus_dir = os.environ["PROMETHEUS_MULTIPROC_DIR"]
else:
    random_id = uuid.uuid4()
    prometheus_dir = f"/tmp/dash_prometheus_{random_id}"
    os.environ["PROMETHEUS_MULTIPROC_DIR"] = prometheus_dir
if os.path.exists(prometheus_dir):
    shutil.rmtree(prometheus_dir)
os.mkdir(prometheus_dir)

from prometheus_client import CollectorRegistry, multiprocess

registry = CollectorRegistry()
multiprocess.MultiProcessCollector(registry, path=prometheus_dir)

from .middleware import add_middleware
from .metrics import counter, histogram
