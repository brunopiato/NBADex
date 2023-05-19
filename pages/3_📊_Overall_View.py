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

filtered_df = pd.read_csv('filtered_df.csv', low_memory=False)


########################################################
#              Layout da barra lateral
########################################################

st.sidebar.image('./pages/NBA_logo_small.png', use_column_width=True)
st.sidebar.markdown('# NBA PlayersDex v.0.2')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown("""---""")




########################################################
#              Layout do corpo da página
########################################################
st.header('Overall statistics by positions')
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.box(filtered_df,
                        x = 'POSITION',
                        y = 'PTS',
                        color = 'POSITION',
                        hover_name='PLAYER_NAME',
                        title = 'Points per Game by Position',
                        labels = {'PTS':'Points', 'POSITION': 'Position'},
                        category_orders = {'POSITION':('G', 'G-F', 'F-G', 'F', 'F-C', 'C-F', 'C')},
                        template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = px.box(filtered_df,
                        x = 'POSITION',
                        y = 'FG3M',
                        color = 'POSITION',
                        hover_name='PLAYER_NAME',
                        title = 'Three points per Game by Position',
                        labels = {'FG3M':'Three points', 'POSITION': 'Position'},
                        category_orders = {'POSITION':('G', 'G-F', 'F-G', 'F', 'F-C', 'C-F', 'C')},
                        template='plotly_dark')
        st.plotly_chart(fig)
        
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(filtered_df,
                        x = 'POSITION',
                        y = 'PF',
                        color = 'POSITION',
                        hover_name='PLAYER_NAME',
                        title = 'Personal fouls per Game by Position',
                        labels = {'PF':'Personal fouls', 'POSITION': 'Position'},
                        category_orders = {'POSITION':('G', 'G-F', 'F-G', 'F', 'F-C', 'C-F', 'C')},
                        template='plotly_dark')
            st.plotly_chart(fig)
            
        with col2:
            fig = px.box(filtered_df,
                        x = 'POSITION',
                        y = 'TOV',
                        color = 'POSITION',
                        hover_name='PLAYER_NAME',
                        title = 'Turn-overs per Game by Position',
                        labels = {'PF':'Turn-overs', 'POSITION': 'Position'},
                        category_orders = {'POSITION':('G', 'G-F', 'F-G', 'F', 'F-C', 'C-F', 'C')},
                        template='plotly_dark')
            st.plotly_chart(fig)
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(filtered_df,
                        x = 'POSITION',
                        y = 'BLK',
                        color = 'POSITION',
                        hover_name='PLAYER_NAME',
                        title = 'Blocks per Game by Position',
                        labels = {'BLK':'Blocks', 'POSITION': 'Position'},
                        category_orders = {'POSITION':('G', 'G-F', 'F-G', 'F', 'F-C', 'C-F', 'C')},
                        template='plotly_dark')
            st.plotly_chart(fig)
            
        with col2:
            fig = px.box(filtered_df,
                        x = 'POSITION',
                        y = 'STL',
                        color = 'POSITION',
                        hover_name='PLAYER_NAME',
                        title = 'Steals per Game by Position',
                        labels = {'STL':'Steals', 'POSITION': 'Position'},
                        category_orders = {'POSITION':('G', 'G-F', 'F-G', 'F', 'F-C', 'C-F', 'C')},
                        template='plotly_dark')
            st.plotly_chart(fig)