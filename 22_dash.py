import dash 
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div([
    html.H1("Gráfico interativo com Dash"),
    dcc.Graph(
        id = "grafico-1",
        figure = {
            "data":[
                go.Scatter(
                    x = [1,2,3,4,5],
                    y = [10,11,12,13,14],
                    mode = "lines+markers",
                    name = "Linha 1"
                ),
                ],
                "layout": go.Layout(
                    title = "Gráfico de linha interativo",
                    xaxis = {"title": "Eixo x"},
                    yaxis = {"title": "Eixo y"}
                )
            }
        )
    ])

if __name__ == "__main__":
    app.run(debug=True)


#dash é uma biblioteca pra trabalhar com dados com fundamento pra framework