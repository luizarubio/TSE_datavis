import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Opções para os checkboxes
idade_disponiveis = [
    {'label': '2014', 'value': 'mapa_2014'},
    {'label': '2016', 'value': 'mapa_2016'},
    {'label': '2018', 'value': 'mapa_2018'},
    {'label': '2020', 'value': 'mapa_2020'},
    {'label': '2022', 'value': 'mapa_2022'},
    {'label': 'entre 2014 e 2022', 'value': 'linhas'},
   
]

distribuicao_disponiveis = [
    {'label': '50k - 2000', 'value': 'mapa_dist_2000'},
    {'label': '100k - 2000', 'value': 'mapa_dist_100_2000'},
    {'label': '50k - 2002', 'value': 'mapa_dist_2002'},
    {'label': '100k - 2002', 'value': 'mapa_dist_100_2002'},
    {'label': '50k - 2004', 'value': 'mapa_dist_2004'},
    {'label': '100k - 2004', 'value': 'mapa_dist_100_2004'},
    {'label': '50k - 2020', 'value': 'mapa_dist_2020'},
    {'label': '100k - 2020', 'value': 'mapa_dist_100_2020'},
    {'label': '50k - 2022', 'value': 'mapa_dist_2022'},
    {'label': '100k - 2022', 'value': 'mapa_dist_100_2022'},
    
]

escolaridade_disponiveis = [
    {'label': 'Por Município - 2012', 'value': 'mapa_mun_2012'},
    {'label': 'Por Estado - 2012', 'value': 'mapa_estado_2012'},
    {'label': 'Por Município - 2014', 'value': 'mapa_mun_2014'},
    {'label': 'Por Estado - 2014', 'value': 'mapa_estado_2014'},
    {'label': 'Por Município - 2016', 'value': 'mapa_mun_2016'},
    {'label': 'Por Estado - 2016', 'value': 'mapa_estado_2016'},
    {'label': 'Por Município - 2018', 'value': 'mapa_mun_2018'},
    {'label': 'Por Estado - 2018', 'value': 'mapa_estado_2018'},
    {'label': 'Por Município - 2020', 'value': 'mapa_mun_2020'},
    {'label': 'Por Estado - 2020', 'value': 'mapa_estado_2020'},
    {'label': 'Por Município - 2022', 'value': 'mapa_mun_2022'},
    {'label': 'Por Estado - 2022', 'value': 'mapa_estado_2022'},
    {'label': 'Por Estado - Animação', 'value': 'mapa_estado_anima'}
    
]



app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="#")),
            dbc.NavItem(dbc.NavLink("Mapas", id="mapas-toggle", n_clicks=0)),
        ],
        brand="Perfil do Eleitorado Brasileiro",
        brand_href="#",
        color="dark",
        dark=True,
        className="ml-auto"  # Mover o menu para a direita
    ),
    dbc.Collapse(
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Idade Média", href="#", id="idade-toggle", n_clicks=0)),
                dbc.Collapse(
                    dbc.Checklist(
                        id='checklist-idade',
                        options=idade_disponiveis,
                        value=[]
                    ),
                    id='idade-collapse',
                    is_open=False,
                    className="ml-3",
                ),
                dbc.NavItem(dbc.NavLink("Distribuição Geográfica", href="#", id="distribuicao-toggle", n_clicks=0)),
                dbc.Collapse(
                    dbc.Checklist(
                        id='checklist-distribuicao',
                        options=distribuicao_disponiveis,
                        value=[]
                    ),
                    id='distribuicao-collapse',
                    is_open=False,
                    className="ml-3",
                ),
                dbc.NavItem(dbc.NavLink("Grau de Escolaridade", href="#", id="escolaridade-toggle", n_clicks=0)),
                dbc.Collapse(
                    dbc.Checklist(
                        id='checklist-escolaridade',
                        options=escolaridade_disponiveis,
                        value=[]
                    ),
                    id='escolaridade-collapse',
                    is_open=False,
                    className="ml-3",
                ),
            ],
            vertical=True,  
            pills=True,
        ),
        id='mapas-menu',
        is_open=False,
    ),
    html.Div(
    id='texto-container',
    children=[
        html.H2("Bem-vindo à Página Inicial!"),
        
        html.P("Esta página é resultado do Trabalho de Conclusão de Curso da aluna Luíza Rubio do curso de Sistemas de Informação da Universidade de São Paulo." ),
        
        html.P( "Selecione no menu os mapas desejados para visualizar os dados do portal de dados abertos do Tribunal Superior Eleitoral a respeito do eleitorado brasileiro."),
    ],
    className="container"
),
    html.Div(id='mapas-container', className='row')
])


@app.callback(
    [Output('mapas-container', 'children'),
     Output('texto-container', 'style')],
    [Input('checklist-idade', 'value'),
     Input('checklist-distribuicao', 'value'),
     Input('checklist-escolaridade', 'value')]
)
def atualizar_mapas(idade_selecionada, distribuicao_selecionada, escolaridade_selecionada):
    mapas = []
    
    for mapa in idade_selecionada:
        if mapa == 'mapa_2014':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_idade_media_2014.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_2016':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_idade_media_2016.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_2018':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_idade_media_2018.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_2020':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_idade_media_2020.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_2022':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_idade_media_2022.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'linhas':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/linhas_idade_2014.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
       
    
    for mapa in distribuicao_selecionada:
        if mapa == 'mapa_dist_2000':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_50k_2000.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_2002':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_50k_2002.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_2004':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_50k_2004.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_2020':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_50k_2020.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_2022':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_50k_2022.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_100_2000':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_100k_2000.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_100_2002':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_100k_2002.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_100_2004':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_100k_2004.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_100_2020':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_100k_2020.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_dist_100_2022':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_distrib_100k_2022.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
    for mapa in escolaridade_selecionada:
        if mapa == 'mapa_mun_2012':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2012.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/bars_mun_sc_2012.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_mun_2012':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2012.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_mun_2014':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2014.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
           
        elif mapa == 'mapa_mun_2016':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2016.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_mun_2018':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2018.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_mun_2020':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2020.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_mun_2022':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_mun_2022.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/bars_mun_sc_2022.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
            
        elif mapa == 'mapa_estado_2014':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_estados_2014.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))

        elif mapa == 'mapa_estado_2016':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridadeestados_2016.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_estado_2018':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_estados_2018.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_estado_2020':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_estados_2020.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_estado_2022':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_estados_2022.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
        elif mapa == 'mapa_estado_anima':
            mapas.append(html.Div(
                html.Iframe(
                    srcDoc=open('C:/Users/Luiza Rubio/Documents/computer science/TCC/deploy/src/htmls/mapa_escolaridade_anima.html', 'r', encoding='utf-8').read(),
                    width='800px',
                    height='500px'
                ),
                className='col-md-6'
            ))
            
     # Verifica se algum mapa foi selecionado
    mapas_selecionados = idade_selecionada + distribuicao_selecionada + escolaridade_selecionada
    texto_visivel = {'display': 'block'} if len(mapas_selecionados) == 0 else {'display': 'none'}
    
    return mapas, texto_visivel


@app.callback(
    Output("mapas-menu", "is_open"),
    [Input("mapas-toggle", "n_clicks")],
    [State("mapas-menu", "is_open")],
)
def toggle_mapas_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("idade-collapse", "is_open"),
    [Input("idade-toggle", "n_clicks")],
    [State("idade-collapse", "is_open")],
)
def toggle_idade_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("distribuicao-collapse", "is_open"),
    [Input("distribuicao-toggle", "n_clicks")],
    [State("distribuicao-collapse", "is_open")],
)
def toggle_distribuicao_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("escolaridade-collapse", "is_open"),
    [Input("escolaridade-toggle", "n_clicks")],
    [State("escolaridade-collapse", "is_open")],
)
def toggle_escolaridade_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
