# `dash-prometheus`

<img src="https://prometheus.io/assets/prometheus_logo_grey.svg" alt="prometheus logo" height="50"/>
<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-plus" width="50" height="50" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M12 5l0 14" /><path d="M5 12l14 0" /></svg>
<img src="https://dash.plotly.com/assets/images/plotly_logo_dark.png" alt="plotly logo" height="50"/>

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
