########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go


########################################################
#              Carregando dados tratados
########################################################

st.set_page_config(page_title = 'Overall Vision', layout='wide', page_icon = '📊')

data = pd.read_csv('df.csv', low_memory=False)


########################################################
#              Layout da barra lateral
########################################################

st.sidebar.image('./pages/NBA_logo_small.png', use_column_width=True)
st.sidebar.markdown('# NBA PlayersDex v.0.1')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown("""---""")




########################################################
#              Layout do corpo da página
########################################################
st.header('Overall statistics by positions')
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.box(data_frame = data,
                        x = 'Pos',
                        y = 'PTS',
                        color = 'Pos',
                        hover_name = 'Player',
                        title = 'Points per Game by Position',
                        labels = {'PTS':'Points per Game',
                                    'Pos':'Position'},
                        category_orders = {'Pos':('PG', 'SG', 'SF', 'PF', 'C', 'PF-SF', 'SF-SG', 'SG-PG')},
                        template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = px.box(data_frame = data,
                        x = 'Pos',
                        y = '3P',
                        color = 'Pos',
                        hover_name = 'Player',
                        title = '3 Points per Game by Position',
                        labels = {'3P':'3 Points per Game',
                                        'Pos':'Position'},
                        category_orders = {'Pos':('PG', 'SG', 'SF', 'PF', 'C', 'PF-SF', 'SF-SG', 'SG-PG')},
                        template='plotly_dark')
        st.plotly_chart(fig)
        
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(data_frame = data,
                            x = 'Pos',
                            y = 'PF',
                            color = 'Pos',
                            hover_name = 'Player',
                            title = 'Personal Fouls per Game by Position',
                            labels = {'PF':'Personal Fouls', 'Pos': 'Position'},
                            category_orders = {'Pos':('PG', 'SG', 'SF', 'PF', 'C', 'PF-SF', 'SF-SG', 'SG-PG')},
                            template='plotly_dark')
            st.plotly_chart(fig)
            
        with col2:
            fig = px.box(data_frame = data,
                            x = 'Pos',
                            y = 'TOV',
                            color = 'Pos',
                            hover_name = 'Player',
                            title = 'Turn-Overs per Game by Position',
                            labels = {'TOV':'Turn-Overs', 'Pos': 'Position'},
                            category_orders = {'Pos':('PG', 'SG', 'SF', 'PF', 'C', 'PF-SF', 'SF-SG', 'SG-PG')},
                            template='plotly_dark')
            st.plotly_chart(fig)
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(data_frame = data,
                            x = 'Pos',
                            y = 'BLK',
                            color = 'Pos',
                            hover_name = 'Player',
                            title = 'Blocks per Game by Position',
                            labels = {'BLK':'Blocks', 'Pos': 'Position'},
                            category_orders = {'Pos':('PG', 'SG', 'SF', 'PF', 'C', 'PF-SF', 'SF-SG', 'SG-PG')},
                            template='plotly_dark')
            st.plotly_chart(fig)
            
        with col2:
            fig = px.box(data_frame = data,
                            x = 'Pos',
                            y = 'STL',
                            color = 'Pos',
                            hover_name = 'Player',
                            title = 'Steals per Game by Position',
                            labels = {'STL':'Steals', 'Pos': 'Position'},
                            category_orders = {'Pos':('PG', 'SG', 'SF', 'PF', 'C', 'PF-SF', 'SF-SG', 'SG-PG')},
                            template='plotly_dark')
            st.plotly_chart(fig)