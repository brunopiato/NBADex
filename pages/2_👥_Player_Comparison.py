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
data = pd.read_csv('transformed_df.csv', low_memory=False)
data_complete = pd.read_csv('filtered_df.csv', low_memory=False)




########################################################
#              Definindo funcoes
########################################################








########################################################
#              Layout da barra lateral
########################################################
st.sidebar.image('./pages/NBA_logo_small.png', use_column_width=True)
st.sidebar.markdown('# NBA PlayersDex v.0.2')
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
                       options=data['PLAYER_NAME'].unique(),
                       index=142)
selected_data_A = data[data['PLAYER_NAME'] == selected_player_A]


# selected_player_B = st.sidebar.text_input(label="Player's name", value='Jayson Tatum')
selected_player_B = st.sidebar.selectbox(label='Select the player', 
                       options=data['PLAYER_NAME'].unique(),
                       index=248)
selected_data_B = data[data['PLAYER_NAME'] == selected_player_B]


selected_data_complete = data_complete[(data_complete['PLAYER_NAME']==selected_player_A) | (data_complete['PLAYER_NAME']==selected_player_B)]
# selected_data_complete = selected_data_complete.drop('Unnamed: 0', axis = 1)



st.sidebar.markdown('##### Powered by Bruno Piato')
#-------------------------- METRICS ------------------------ #
team_A = selected_data_A['TEAM_ABBREVIATION'].iloc[0]
position_A = selected_data_A['POSITION'].iloc[0]
age_A = selected_data_A['AGE'].iloc[0].astype(int)
plus_minus_A = selected_data_A['PLUS_MINUS'].iloc[0]
country_A = selected_data_A['COUNTRY'].iloc[0]
height_A = selected_data_A['PLAYER_HEIGHT_CM'].iloc[0].astype(int)
weight_A = selected_data_A['PLAYER_WEIGHT_KG'].iloc[0]
draft_A = selected_data_A['DRAFT_YEAR'].iloc[0]
number_A = selected_data_A['JERSEY_NUMBER'].iloc[0].astype(int)

team_B = selected_data_B['TEAM_ABBREVIATION'].iloc[0]
position_B = selected_data_B['POSITION'].iloc[0]
age_B = selected_data_B['AGE'].iloc[0].astype(int)
plus_minus_B = selected_data_B['PLUS_MINUS'].iloc[0]
country_B = selected_data_B['COUNTRY'].iloc[0]
height_B = selected_data_B['PLAYER_HEIGHT_CM'].iloc[0].astype(int)
weight_B = selected_data_B['PLAYER_WEIGHT_KG'].iloc[0]
draft_B = selected_data_B['DRAFT_YEAR'].iloc[0]
number_B = selected_data_B['JERSEY_NUMBER'].iloc[0].astype(int)


#-------------------------- FEATURES ------------------------ #
offensive_features = ['PTS', 'AST', 'FG_PCT', 'FG3_PCT', 'FT_PCT', ]
defensive_features = ['OREB', 'DREB', 'STL', 'BLK', 'CONTESTED_SHOTS', 'BOX_OUTS', 'CHARGES_DRAWN']
descriptive_features = ['GP', 'MIN', 'PF', 'PFD', 'TOV', 'REB']


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
                st.text(f'Country: {country_A}')
                st.text(f'Height(cm): {height_A}')
                st.text(f'Weight(kg): {weight_A}')

            with col5: 
                st.text(f'Plus/Minus: {round(plus_minus_A, 3)}')
                st.text(f'Drafted in: {draft_A}')
                st.text(f'Jersey Number: {number_A}')
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
                st.text(f'Country: {country_B}')
                st.text(f'Height(cm): {height_B}')
                st.text(f'Weight(kg): {weight_B}')

            with col8: 
                st.text(f'Plus/Minus: {round(plus_minus_B, 3)}')
                st.text(f'Drafted in: {draft_B}')
                st.text(f'Jersey Number: {number_B}')
        
        
        

st.markdown("---")

# ----------------------------------------------------------------    
with st.container():
    # st.markdown('## Chart', )
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # st.markdown('### Offensive')
        aux_A = selected_data_A[selected_data_A['PLAYER_NAME'] == selected_player_A][offensive_features].T
        aux_A.columns = [selected_player_A]

        aux_B = selected_data_B[selected_data_B['PLAYER_NAME'] == selected_player_B][offensive_features].T
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
        
        fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01),
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 1]
                )),
            showlegend=True,
            width=800, height=650,
            template="plotly_dark",
            title = 'Offensive Features'
            )

        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------------    
    with col2:
        # st.markdown('### Defensive')
        aux_A = selected_data_A[selected_data_A['PLAYER_NAME'] == selected_player_A][offensive_features].T
        aux_A.columns = [selected_player_A]

        aux_B = selected_data_B[selected_data_B['PLAYER_NAME'] == selected_player_B][offensive_features].T
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
        
        fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01),
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 1]
                )),
            showlegend=True,
            width=800, height=650,
            template="plotly_dark",
            title = 'Defensive Features'
            )

        st.plotly_chart(fig, use_container_width=True)

        
# ----------------------------------------------------------------    
    with col3:
        # st.markdown('### Other Features')
        aux_A = selected_data_A[selected_data_A['PLAYER_NAME'] == selected_player_A][offensive_features].T
        aux_A.columns = [selected_player_A]

        aux_B = selected_data_B[selected_data_B['PLAYER_NAME'] == selected_player_B][offensive_features].T
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
        
        fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01),
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 1]
                )),
            showlegend=True,
            width=800, height=650,
            template="plotly_dark",
            title = 'Descriptive Features'
            )

        st.plotly_chart(fig, use_container_width=True)
# ----------------------------------------------------------------

with st.container():
    st.dataframe(selected_data_complete)