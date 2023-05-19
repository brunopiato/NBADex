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

#Vinculando os widgets aos dados
# selected_rows = data['Tm'].isin(selected_teams)
# data = data.loc[selected_rows, :]
# selected_rows = data['Pos'].isin(selected_positions)
# data = data.loc[selected_rows, :]
# selected_rows = data[data['Player'] == selected_player]
# # data = data.loc[selected_rows, :]




#---------------------- Player selection ------------------- #
#### Setting the widget
selected_player = st.sidebar.selectbox(label='Select the player', 
                       options=data['PLAYER_NAME'].unique())

# selected_player = st.sidebar.text_input(label="Player's name", value='Joel Embiid')

#### Filtering the dataset
selected_data = data[data['PLAYER_NAME'] == selected_player]
st.sidebar.markdown('##### Powered by Bruno Piato')

selected_data_complete = data_complete[data_complete['PLAYER_NAME']==selected_player]
# selected_data_complete = selected_data_complete.drop('Unnamed: 0', axis = 1)


#-------------------------- METRICS ------------------------ #
team = selected_data['TEAM_ABBREVIATION'].iloc[0]
position = selected_data['POSITION'].iloc[0]
age = selected_data['AGE'].iloc[0].astype(int)
plus_minus = selected_data['PLUS_MINUS'].iloc[0]
country = selected_data['COUNTRY'].iloc[0]
height = selected_data['PLAYER_HEIGHT_CM'].iloc[0].astype(int)
weight = selected_data['PLAYER_WEIGHT_KG'].iloc[0]
draft = selected_data['DRAFT_YEAR'].iloc[0]
number = selected_data['JERSEY_NUMBER'].iloc[0].astype(int)


#-------------------------- FEATURES ------------------------ #
offensive_features = ['PTS', 'AST', 'FG_PCT', 'FG3_PCT', 'FT_PCT', ]
defensive_features = ['OREB', 'DREB', 'STL', 'BLK', 'CONTESTED_SHOTS', 'BOX_OUTS', 'CHARGES_DRAWN']
descriptive_features = ['GP', 'MIN', 'PF', 'PFD', 'TOV', 'REB']

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
        # st.markdown('#### Team, Position and age')
        st.text(f'Team: {team}')
        st.text(f'Position: {position}')
        st.text(f'Age: {age}')

    # ----------------------------------------------------------------    
    with col2:
        # st.markdown('#### Country, height and weight')
        st.text(f'Country: {country}')
        st.text(f'Height(cm): {height}')
        st.text(f'Weight(kg): {weight}')

    # ----------------------------------------------------------------    
    with col3: 
        # st.markdown('#### Nationality, Plus/Minus and draft')
        st.text(f'Plus/Minus: {round(plus_minus, 3)}')
        st.text(f'Drafted in: {draft}')
        st.text(f'Jersey Number: {number}')

        
st.markdown("---")

# ----------------------------------------------------------------    
with st.container():
    # st.markdown('## Chart', )
    col1, col2, col3 = st.columns(3)
    # ----------------------------------------------------------------    
    with col1:
        # st.markdown('### Offensive')
        aux = selected_data[selected_data['PLAYER_NAME'] == selected_player][offensive_features].T
        aux.columns = [selected_player]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=aux[selected_player],
            theta=offensive_features,
            fill='toself',
            name=selected_player
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
        aux = selected_data[selected_data['PLAYER_NAME'] == selected_player][defensive_features].T
        aux.columns = [selected_player]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=aux[selected_player],
            theta=defensive_features,
            fill='toself',
            name=selected_player
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
        aux = selected_data[selected_data['PLAYER_NAME'] == selected_player][descriptive_features].T
        aux.columns = [selected_player]
        
        # plt.rcParams['figure.figsize'] = [4, 4]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=aux[selected_player],
            theta=descriptive_features,
            fill='toself',
            name=selected_player
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