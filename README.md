# ![promehteus logo](https://prometheus.io/assets/prometheus_logo_grey.svg) `dash-prometheus`

Producing Prometheus stats fro DASH (plotly) apps.

## Installation

```bash
pip install git+https://github.com/gitHBDX/dash-prometheus.git
```

then in your DASH app

```python
#  dash_prometheus has to be imported before dash
import dash_prometheus

...

app = dash.Dash(...)
dash_prometheus.add_middleware(app)
```

The Prometheus endpoint is exposed on the same host/port on `/metrics` but can be configured when adding the middleware.

## Metrics

Currently produces the following metrics:

| Type | Name | Description | Labels |
| ---- | ---- | ----------- | ------ |
| Counter | `dash_callback_calls` | Number of calls to a Dash callback | `module`, `callback` |
| Histogram | `dash_callback_duration` | Duration of Dash callback | `module`, `callback` |


-----

<p>Developed @</p>
<img src="https://www.hummingbird-diagnostics.com/application/files/4214/6893/9202/logo.png" alt="Hummingbid Diagnostics logo" width="200"/>
