########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
import numpy as np
import shapely.geometry as sg
import funcoes

st.set_page_config(page_title = 'Shot Charts Comparison', layout='wide', page_icon = '📈')

########################################################
#              Carregando dados tratados
########################################################

data = pd.read_csv('transformed_df.csv', low_memory=False)
data_complete = pd.read_csv('filtered_df.csv', low_memory=False)




########################################################
#              Layout da barra lateral
########################################################
st.sidebar.image('./pages/NBA_logo_small.png', use_column_width=True)
st.sidebar.markdown('# NBA PlayersDex v.0.2')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown("""---""")


#---------------------- Player selection ------------------- #
#### Setting the widget
selected_player_A = st.sidebar.selectbox(label='Select the first player', 
                       options=data['PLAYER_NAME'].unique(),
                       index=252)
selected_data_A = data[data['PLAYER_NAME'] == selected_player_A]
selected_data_complete_A = data_complete[(data_complete['PLAYER_NAME']==selected_player_A)]

selected_player_B = st.sidebar.selectbox(label='Select the second player', 
                       options=data['PLAYER_NAME'].unique(),
                       index=166)
selected_data_B = data[data['PLAYER_NAME'] == selected_player_B]
selected_data_complete_B = data_complete[(data_complete['PLAYER_NAME']==selected_player_B)]

selected_data_complete = data_complete[(data_complete['PLAYER_NAME']==selected_player_A) | (data_complete['PLAYER_NAME']==selected_player_B)]


#-------------------------- METRICS ------------------------ #

### Getting data from the API
playerA_shotchart_df, league_avg = funcoes.get_player_shotchartdetail(player_name=selected_player_A, season_id='2022-23')
playerB_shotchart_df, league_avg = funcoes.get_player_shotchartdetail(player_name=selected_player_B, season_id='2022-23')


event_type_filter_player = st.sidebar.multiselect(label='Select the event type',
                       options=set(playerA_shotchart_df['EVENT_TYPE']),
                       default=playerA_shotchart_df['EVENT_TYPE'].unique())
action_type_filter_player = st.sidebar.multiselect(label='Select the action type',
                       options=set(playerA_shotchart_df['ACTION_TYPE']),
                       default=playerA_shotchart_df['ACTION_TYPE'].unique())


playerA_shotchart_df_filtered = playerA_shotchart_df[(playerA_shotchart_df['EVENT_TYPE'].isin(event_type_filter_player)) & 
                                                   (playerA_shotchart_df['ACTION_TYPE'].isin(action_type_filter_player))].reset_index()

playerB_shotchart_df_filtered = playerB_shotchart_df[(playerB_shotchart_df['EVENT_TYPE'].isin(event_type_filter_player)) & 
                                                   (playerB_shotchart_df['ACTION_TYPE'].isin(action_type_filter_player))].reset_index()



st.sidebar.markdown('##### Powered by Bruno Piato')
########################################################
#              Layout do corpo da página
########################################################

st.markdown("""
            # Shot Charts
            Shot charts are a very effective way to visualize a player's accuracy, preferred shooting positions and most effective areas on court.
            
            In this page you can select two players to compare as well as choose only two pointers, three pointer or both. You can also select the type of action the player took to make the shot attempt.
            """)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label='',
                value=f'{selected_player_A}')
        plt.rcParams['figure.figsize'] = (8, 8/1.09)
        fig_shotchart = funcoes.shot_chart(playerA_shotchart_df_filtered, 
                                            title="{0}            FG%: {1}".format(playerA_shotchart_df_filtered['PLAYER_NAME'][0], 
                                                                                   selected_data_A['FG_PCT'].iloc[0]), 
                                            flip_court=False,
                                            court_lw=2)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(use_container_width=True)
        
    with col2:
        st.metric(label='',
                value=f'{selected_player_B}')
        plt.rcParams['figure.figsize'] = (8, 8/1.09)
        fig_shotchart = funcoes.shot_chart(playerB_shotchart_df_filtered, 
                                            title="{0}            FG%: {1}".format(playerB_shotchart_df_filtered['PLAYER_NAME'][0], 
                                                                                   selected_data_B['FG_PCT'].iloc[0]), 
                                            flip_court=False,
                                            court_lw=2)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(use_container_width=True)

        
st.markdown("---")

# ----------------------------------------------------------------    

with st.container():
    st.dataframe(selected_data_complete)
