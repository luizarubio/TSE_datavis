import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import requests
import json

# Define the API URL and parameters
url = "https://api.tse.jus.br/partidos/filiados/uf/2014"
headers = {"Accept": "application/json"}

# Send a GET request to the API and convert the response to a DataFrame
response = requests.get(url, headers=headers)
data = json.loads(response.content)
df = pd.json_normalize(data)

# Define the Dash app and its layout
app = dash.Dash(__name__, name='Dash_Waffle')
server = app.server

app.layout = html.Div([
    html.H1("Brazilian Political Parties Budgets"),
    dcc.Graph(id="waffle-chart"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[
            {"label": "2014", "value": "2014"},
            {"label": "2016", "value": "2016"},
            {"label": "2018", "value": "2018"},
            {"label": "2020", "value": "2020"}
        ],
        value="2014"
    )
])

# Define the callback function to update the waffle chart based on the year dropdown
@app.callback(Output("waffle-chart", "figure"), [Input("year-dropdown", "value")])
def update_waffle_chart(year):
    # Filter the DataFrame to the selected year
    df_year = df[df["ano"] == int(year)]
    
    # Aggregate the budget by political party and calculate the percentage of the total
    df_agg = df_year.groupby("siglaPartido").agg({"valorDespesa": "sum"}).reset_index()
    df_agg["percent"] = df_agg["valorDespesa"] / df_agg["valorDespesa"].sum()
    
    # Create the waffle chart using Plotly Express
    fig = px.pie(df_agg, values="percent", names="siglaPartido")
    fig.update_traces(hoverinfo="label+percent", textinfo="value", textfont_size=18)
    fig.update_layout(title=f"Brazilian Political Parties Budgets in {year}", height=500)
    fig.update_yaxes(showticklabels=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(annotations=[dict(text="100%", x=0.5, y=0.5, font_size=40, showarrow=False)])
    
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)