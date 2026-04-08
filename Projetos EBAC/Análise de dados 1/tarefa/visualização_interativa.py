import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Carregar dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Criar lista de opções para o dropdown
lista_qtd_vendidos = df['Qtd_Vendidos_Cod'].unique()
options = [{'label': str(nivel), 'value': nivel} for nivel in lista_qtd_vendidos]

# Inicializar o app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Interativa"),

    # Dropdown para filtro
    dcc.Dropdown(
        id='dropdown-vendidos',
        options=options,
        value=lista_qtd_vendidos[0],  # valor inicial
        clearable=False
    ),

    # Gráficos interativos
    dcc.Graph(id='histograma'),
    dcc.Graph(id='dispersao')
])

# Callbacks para atualizar os gráficos
@app.callback(
    [Output('histograma', 'figure'),
     Output('dispersao', 'figure')],
    [Input('dropdown-vendidos', 'value')]
)
def update_graphs(selected_value):
    # Filtrar dados
    dff = df[df['Qtd_Vendidos_Cod'] == selected_value]

    # 1. Histograma com Plotly Express
    fig_hist = px.histogram(
        dff, x="Preço",
        nbins=20,
        title="Histograma de Preço",
        color_discrete_sequence=["skyblue"]
    )

    # 2. Dispersão com Plotly Express
    fig_disp = px.scatter(
        dff, x="Preço", y="Nota",
        title="Preço vs Nota",
        color_discrete_sequence=["purple"],
        opacity=0.6
    )

    return fig_hist, fig_disp

if __name__ == '__main__':
    app.run(debug=True)
