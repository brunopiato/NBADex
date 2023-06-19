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

st.set_page_config(page_title = 'Single Player Vision', layout='wide', page_icon = '📈')

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
selected_player = st.sidebar.selectbox(label='Select the player', 
                       options=data['PLAYER_NAME'].unique(),
                       index=252)
selected_data = data[data['PLAYER_NAME'] == selected_player]
selected_data_complete = data_complete[data_complete['PLAYER_NAME']==selected_player]


#-------------------------- METRICS ------------------------ #
team = selected_data['TEAM_ABBREVIATION'].iloc[0]
position = selected_data['POSITION'].iloc[0]
age = selected_data['AGE'].iloc[0].astype(int)
number = selected_data['JERSEY_NUMBER'].iloc[0].astype(int)
points = selected_data_complete['PTS'].iloc[0]
blocks = selected_data_complete['BLK'].iloc[0]
assists = selected_data_complete['AST'].iloc[0]
games_played = selected_data_complete['G'].iloc[0]


### Getting data from the API
player_shotchart_df, league_avg = funcoes.get_player_shotchartdetail(player_name=selected_player, season_id='2022-23')
player_shotchart_df, league_avg = funcoes.get_player_shotchartdetail(player_name=selected_player, season_id='2022-23')

event_type_filter = st.sidebar.multiselect(label='Select the event type',
                       options=set(player_shotchart_df['EVENT_TYPE']),
                       default=player_shotchart_df['EVENT_TYPE'].unique())

action_type_filter = st.sidebar.multiselect(label='Select the action type',
                       options=set(player_shotchart_df['ACTION_TYPE']),
                       default=player_shotchart_df['ACTION_TYPE'].unique())

player_shotchart_df_filtered = player_shotchart_df[(player_shotchart_df['EVENT_TYPE'].isin(event_type_filter)) & 
                                                   (player_shotchart_df['ACTION_TYPE'].isin(action_type_filter))].reset_index()



st.sidebar.markdown('##### Powered by Bruno Piato')
########################################################
#              Layout do corpo da página
########################################################

# st.header("👤 Single Player Vision")

# st.subheader("Player's name")
st.metric(label='',
          value=f'{selected_player}')
    # ----------------------------------------------------------------    
    
with st.container():
    col1, col2, col3 = st.columns([4,10,4])
    with col1:
        st.empty()
        
    with col2:
        # st.markdown(f"##### {selected_player}'s Shot Chart")
        plt.rcParams['figure.figsize'] = (8, 8/1.09)
        fig_shotchart = funcoes.shot_chart(player_shotchart_df_filtered, 
                                            title="{[0]}".format(player_shotchart_df_filtered['PLAYER_NAME']), 
                                            flip_court=False,
                                            court_lw=2)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(use_container_width=True)
        
    with col3:
        st.empty()
        
st.markdown("---")

# ----------------------------------------------------------------    

with st.container():
    st.dataframe(selected_data_complete)
