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
# selected_player = st.sidebar.selectbox(label='Select the player', 
#                        options=data['Player'].unique())
#Vinculando os widgets aos dados
# selected_rows = data['Tm'].isin(selected_teams)
# data = data.loc[selected_rows, :]
# selected_rows = data['Pos'].isin(selected_positions)
# data = data.loc[selected_rows, :]
# selected_rows = data[data['Player'] == selected_player]
# # data = data.loc[selected_rows, :]




#---------------------- Player selection ------------------- #
# selected_player_A = st.sidebar.text_input(label="Player's name", value='Joel Embiid')
selected_player_A = st.sidebar.selectbox(label='Select the player', 
                       options=data['Player'].unique(),
                       index=142)
selected_data_A = data[data['Player'] == selected_player_A]


# selected_player_B = st.sidebar.text_input(label="Player's name", value='Jayson Tatum')
selected_player_B = st.sidebar.selectbox(label='Select the player', 
                       options=data['Player'].unique(),
                       index=248)
selected_data_B = data[data['Player'] == selected_player_B]



st.sidebar.markdown('##### Powered by Bruno Piato')


#-------------------------- METRICS ------------------------ #
team_A = selected_data_A['Tm'].iloc[0]
position_A = selected_data_A['Pos'].iloc[0]
age_A = selected_data_A['Age'].iloc[0]
vorp_A = selected_data_A['VORP'].iloc[0]
obpm_A = selected_data_A['OBPM'].iloc[0]
dbpm_A = selected_data_A['DBPM'].iloc[0]
bpm_A = selected_data_A['BPM'].iloc[0]



team_B = selected_data_B['Tm'].iloc[0]
position_B = selected_data_B['Pos'].iloc[0]
age_B = selected_data_B['Age'].iloc[0]
vorp_B = selected_data_B['VORP'].iloc[0]
obpm_B = selected_data_B['OBPM'].iloc[0]
dbpm_B = selected_data_B['DBPM'].iloc[0]
bpm_B = selected_data_B['BPM'].iloc[0]




########################################################
#              Layout do corpo da página
########################################################

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label='',
            value=f'{selected_player_A}')
        with st.container():
            col3, col4, col5 = st.columns(3)
            with col3:
                # st.markdown('#### Team and Position')
                st.text(f'Team: {team_A}')
                st.text(f'Position: {position_A}')
                st.text(f'Age: {age_A}')

            with col4:
                # st.markdown('#### Age and score')
                st.text(f'VORP Rank: {round(vorp_A, 3)}')
                st.text(f'BPM: {round(bpm_A, 3)}')

            with col5: 
                # st.markdown('#### Info 1 e 2')
                st.text(f'OBPM: {round(obpm_A, 3)}')
                st.text(f'DBPM: {round(dbpm_A, 3)}')
# ----------------------------------------------------------------        
    with col2:
        st.metric(label='',
            value=f'{selected_player_B}')
        with st.container():
            col6, col7, col8 = st.columns(3)
            with col6:
                # st.markdown('#### Team and Position')
                st.text(f'Team: {team_B}')
                st.text(f'Position: {position_B}')
                st.text(f'Age: {age_B}')

            with col7:
                # st.markdown('#### Age and score')
                st.text(f'VORP Rank: {round(vorp_B, 3)}')
                st.text(f'BPM: {round(bpm_B, 3)}')

            with col8: 
                # st.markdown('#### Info 1 e 2')
                st.text(f'OBPM: {round(obpm_B, 3)}')
                st.text(f'DBPM: {round(dbpm_B, 3)}')
        
        
        

st.markdown("---")

# ----------------------------------------------------------------    
with st.container():
    # st.markdown('## Chart', )
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # st.markdown('### Offensive')
        offensive_features = ['PTS', 'FT%', '2P%', '3P%', 'TS%', 'AST', 'OWS']
        
        aux_A = selected_data_A[selected_data_A['Player'] == selected_player_A][offensive_features].T
        aux_A.columns = [selected_player_A]

        aux_B = selected_data_B[selected_data_B['Player'] == selected_player_B][offensive_features].T
        aux_B.columns = [selected_player_B]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=aux_A[selected_player_A],
            theta=offensive_features,
            fill='toself',
            name=selected_player_A
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=aux_B[selected_player_B],
            theta=offensive_features,
            fill='toself',
            name=selected_player_B
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
        
        aux_A = selected_data_A[selected_data_A['Player'] == selected_player_A][offensive_features].T
        aux_A.columns = [selected_player_A]

        aux_B = selected_data_B[selected_data_B['Player'] == selected_player_B][offensive_features].T
        aux_B.columns = [selected_player_B]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=aux_A[selected_player_A],
            theta=defensive_features,
            fill='toself',
            name=selected_player_A
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=aux_B[selected_player_B],
            theta=defensive_features,
            fill='toself',
            name=selected_player_B
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
    with col3:
        # st.markdown('### Other Features')
        descriptive_features = ['TOV', 'GM', 'PF', 'G', 'MP', 'WS', 'VORP']
        
        aux_A = selected_data_A[selected_data_A['Player'] == selected_player_A][offensive_features].T
        aux_A.columns = [selected_player_A]

        aux_B = selected_data_B[selected_data_B['Player'] == selected_player_B][offensive_features].T
        aux_B.columns = [selected_player_B]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=aux_A[selected_player_A],
            theta=descriptive_features,
            fill='toself',
            name=selected_player_A
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=aux_B[selected_player_B],
            theta=descriptive_features,
            fill='toself',
            name=selected_player_B
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

        

