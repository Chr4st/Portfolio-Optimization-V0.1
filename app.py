import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

# Load data
max_sharpe = pd.read_csv("./outputs/results/max_sharpe_portfolio_value.csv", index_col=0, parse_dates=True).squeeze("columns")
high_growth = pd.read_csv("./outputs/results/high_growth_portfolio_value.csv", index_col=0, parse_dates=True).squeeze("columns")
dca = pd.read_csv("./outputs/results/dca_simulation_high_growth.csv", index_col=0, parse_dates=True).squeeze("columns")

sharpe_weights = pd.read_csv("./data/processed/max_sharpe_weights.csv", index_col=0).squeeze("columns")
growth_weights = pd.read_csv("./data/processed/high_growth_weights.csv", index_col=0).squeeze("columns")

# Dash app with Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Portfolio Dashboard"

# Strategy map
data_map = {
    "Max Sharpe": max_sharpe,
    "High Growth": high_growth,
    "DCA ($100/mo)": dca
}

weight_map = {
    "Max Sharpe": sharpe_weights,
    "High Growth": growth_weights
}

# App layout
app.layout = dbc.Container([
    html.H1("Portfolio Strategy Dashboard", className="my-4 text-center"),

    dbc.Row([
        dbc.Col([
            html.Label("Select Strategy", className="fw-bold"),
            dcc.Dropdown(
                id='strategy-dropdown',
                options=[{'label': k, 'value': k} for k in data_map.keys()],
                value='High Growth',
                clearable=False
            ),
            html.Div(id='metrics-output', className="mt-4"),
        ], width=3),

        dbc.Col([
            dcc.Graph(id='value-chart'),
        ], width=9)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='allocation-pie')
        ])
    ], className="mt-4")
], fluid=True)

# Callback
@app.callback(
    Output('value-chart', 'figure'),
    Output('allocation-pie', 'figure'),
    Output('metrics-output', 'children'),
    Input('strategy-dropdown', 'value')
)
def update_dashboard(strategy):
    data = data_map[strategy]
    returns = data.pct_change().dropna()

    cum_return = (data.iloc[-1] / data.iloc[0]) - 1
    vol = returns.std() * np.sqrt(252)
    sharpe = (returns.mean() * 252 - 0.02) / (returns.std() * np.sqrt(252))

    # Line chart
    value_fig = px.line(data, title=f"Portfolio Value - {strategy}", labels={'value': 'Portfolio Value'})
    value_fig.update_layout(margin=dict(t=40, b=20, l=20, r=20))

    # Pie chart
    if strategy in weight_map:
        weights = weight_map[strategy][weight_map[strategy] > 0.01].sort_values()
        pie_fig = px.pie(weights, values=weights.values, names=weights.index, title="Portfolio Allocation")
    else:
        pie_fig = go.Figure()
        pie_fig.update_layout(title="No Allocation Data for DCA")

    # Stat boxes
    metrics = dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Cumulative Return", className="card-title text-success"),
                html.H4(f"{cum_return:.2%}", className="card-text")
            ])
        ], color="light", className="mb-2")),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Annual Volatility", className="card-title text-warning"),
                html.H4(f"{vol:.2%}", className="card-text")
            ])
        ], color="light", className="mb-2")),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Sharpe Ratio", className="card-title text-primary"),
                html.H4(f"{sharpe:.2f}", className="card-text")
            ])
        ], color="light", className="mb-2")),
    ])

    return value_fig, pie_fig, metrics

if __name__ == '__main__':
   app.run(debug=True)
