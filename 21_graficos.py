import plotly.graph_objs as go
#Gera gráficos
#Pode combinar com Flask
#Sempre tem que olhar a documentação
eixo_x = [1,2,3,4,5]
eixo_y = [10,11,12,13,14]

#criando um gráfico de linha
fig = go.Figure(
    data=go.Scatter(
        x=eixo_x,
        y=eixo_y,
        mode = "lines + markers",
        name = "linha 1"
        )
    )

fig.update_layout(
    title = "Gráfico de linha interativo",
    xaxis_title = "Unidades",
    yaxis_title = "Dezenas"
)

fig.show()