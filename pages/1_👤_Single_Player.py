########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(page_title = 'Single Player Vision', layout='wide', page_icon = '👤')

########################################################
#              Carregando dados tratados
########################################################

data = pd.read_csv('df_selected.csv', low_memory=False)




########################################################
#              Definindo funcoes
########################################################








########################################################
#              Layout da barra lateral
########################################################
st.sidebar.image('./pages/NBA_logo_small.png', use_column_width=True)
st.sidebar.markdown('# NBA PlayersDex v.0.1')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown("""---""")


# ------------------------------------------------------
# -------------- Widgets -------------------------------
# ------------------------------------------------------
# selected_teams = st.sidebar.multiselect(label='Select the team(s)', 
#                        options=data['Tm'].unique(),
#                        default = [])
# selected_positions = st.sidebar.multiselect(label='Select the position(s)', 
#                        options=data['Pos'].unique(),
#                        default = [])

#Vinculando os widgets aos dados
# selected_rows = data['Tm'].isin(selected_teams)
# data = data.loc[selected_rows, :]
# selected_rows = data['Pos'].isin(selected_positions)
# data = data.loc[selected_rows, :]
# selected_rows = data[data['Player'] == selected_player]
# # data = data.loc[selected_rows, :]




#---------------------- Player selection ------------------- #

selected_player = st.sidebar.selectbox(label='Select the player', 
                       options=data['Player'].unique())

# selected_player = st.sidebar.text_input(label="Player's name", value='Joel Embiid')


selected_data = data[data['Player'] == selected_player]
st.sidebar.markdown('##### Powered by Bruno Piato')



#-------------------------- METRICS ------------------------ #
team = selected_data['Tm'].iloc[0]
position = selected_data['Pos'].iloc[0]
age = selected_data['Age'].iloc[0]
vorp = selected_data['VORP'].iloc[0]
obpm = selected_data['OBPM'].iloc[0]
dbpm = selected_data['DBPM'].iloc[0]
bpm = selected_data['BPM'].iloc[0]



########################################################
#              Layout do corpo da página
########################################################

# st.header("👤 Single Player Vision")

# st.subheader("Player's name")
st.metric(label='',
          value=f'{selected_player}')
    # ----------------------------------------------------------------    
    
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        # st.markdown('#### Team and Position')
        st.text(f'Team: {team}')
        st.text(f'Position: {position}')
        st.text(f'Age: {age}')

    # ----------------------------------------------------------------    
    with col2:
        # st.markdown('#### Age and score')
     
        st.text(f'VORP Rank: {round(vorp, 3)}')
        st.text(f'BPM: {round(bpm, 3)}')

    # ----------------------------------------------------------------    
    with col3: 
        # st.markdown('#### Info 1 e 2')
        st.text(f'OBPM: {round(obpm, 3)}')
        st.text(f'DBPM: {round(dbpm, 3)}')
        
st.markdown("---")

# ----------------------------------------------------------------    
with st.container():
    # st.markdown('## Chart', )
    col1, col2, col3 = st.columns(3)
    # ----------------------------------------------------------------    
    with col1:
        # st.markdown('### Offensive')
        offensive_features = ['PTS', 'FT%', '2P%', '3P%', 'TS%', 'AST', 'OWS']
        
        aux = selected_data[selected_data['Player'] == selected_player][offensive_features].T
        aux.columns = [selected_player]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=aux[selected_player],
            theta=offensive_features,
            fill='toself',
            name=selected_player
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 1]
                )),
            showlegend=False,
            width=800, height=800,
            template="plotly_dark",
            title = 'Offensive Features'
            )

        st.plotly_chart(fig, use_container_width=True)
        

    # ----------------------------------------------------------------    
    with col2:
        # st.markdown('### Defensive')
        defensive_features = ['ORB', 'DRB', 'STL', 'BLK', 'DWS']
        
        aux = selected_data[selected_data['Player'] == selected_player][defensive_features].T
        aux.columns = [selected_player]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=aux[selected_player],
            theta=defensive_features,
            fill='toself',
            name=selected_player
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 1]
                )),
            showlegend=False,
            width=800, height=800,
            template="plotly_dark",
            title = 'Defensive Features'
            )
        
        st.plotly_chart(fig, use_container_width=True)
        
    # ----------------------------------------------------------------    
    with col3:
        # st.markdown('### Other Features')
        descriptive_features = ['TOV', 'GM', 'PF', 'G', 'MP', 'WS', 'VORP']
        
        aux = selected_data[selected_data['Player'] == selected_player][descriptive_features].T
        aux.columns = [selected_player]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=aux[selected_player],
            theta=descriptive_features,
            fill='toself',
            name=selected_player
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 1]
                )),
            showlegend=False,
            width=800, height=800,
            template="plotly_dark",
            title = 'Descriptive Features'
            )
        
        st.plotly_chart(fig, use_container_width=True)
        

