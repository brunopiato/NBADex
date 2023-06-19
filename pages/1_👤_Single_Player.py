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
#                        options=data['TEAM_ABBREVIATION'].unique(),
#                        default = [])
# selected_positions = st.sidebar.multiselect(label='Select the position(s)', 
#                        options=data['POSITION'].unique(),
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
                       options=data['PLAYER_NAME'].unique(),
                       index=252)
selected_data = data[data['PLAYER_NAME'] == selected_player]
selected_data_complete = data_complete[data_complete['PLAYER_NAME']==selected_player]


st.sidebar.markdown('##### Powered by Bruno Piato')
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
points = selected_data_complete['PTS'].iloc[0]
blocks = selected_data_complete['BLK'].iloc[0]
assists = selected_data_complete['AST'].iloc[0]
games_played = selected_data_complete['G'].iloc[0]


#---------------------- FEATURE SELECTION ------------------- #
offensive_features = ['PTS', 'AST', 'FG_PCT', 'FG3_PCT', 'FT_PCT', ]
defensive_features = ['OREB', 'DREB', 'STL', 'BLK', 'CONTESTED_SHOTS', 'BOX_OUTS', 'CHARGES_DRAWN']
descriptive_features = ['GP', 'MIN', 'PF', 'PFD', 'TOV', 'REB']


# ----------------- DATA PREPARATION ------------------------- # 
# CHARTS DATA
# Offensive features
aux_off = selected_data[selected_data['PLAYER_NAME'] == selected_player][offensive_features].T
aux_off.columns = [selected_player]
# Defensive features
aux_def = selected_data[selected_data['PLAYER_NAME'] == selected_player][defensive_features].T
aux_def.columns = [selected_player]
# Descriptive features
aux_desc = selected_data[selected_data['PLAYER_NAME'] == selected_player][descriptive_features].T
aux_desc.columns = [selected_player]

# DEFINING FIGURES
# Offensive chart
fig_off = go.Figure()
fig_off.add_trace(go.Scatterpolar(
    r=aux_off[selected_player],
    theta=offensive_features,
    fill='toself',
    name=selected_player))
fig_off.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01),
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 1])),
    showlegend=True,
    width=800, height=650,
    template="plotly_dark",
    title = 'Offensive Features')

# Defensive chart
fig_def = go.Figure()
fig_def.add_trace(go.Scatterpolar(
    r=aux_def[selected_player],
    theta=defensive_features,
    fill='toself',
    name=selected_player))
fig_def.update_layout(legend=dict(
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
    title = 'Defensive Features')

# Descriptive chart
fig_desc = go.Figure()
fig_desc.add_trace(go.Scatterpolar(
    r=aux_desc[selected_player],
    theta=descriptive_features,
    fill='toself',
    name=selected_player))
fig_desc.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01),
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 1])),
    showlegend=True,
    width=800, height=650,
    template="plotly_dark",
    title = 'Descriptive Features')


# POLYGON AREA DATA
# Offensive chart
df_off = pd.concat([pd.DataFrame({"r": t.r, 
                      "theta": t.theta, 
                      "trace": np.full(len(t.r), t.name)})
        for t in fig_off.data])
df_off["theta_n"] = pd.factorize(df_off["theta"])[0]
df_off["theta_radian"] = (df_off["theta_n"] / (df_off["theta_n"].max() + 1)) * 2 * np.pi
df_off["x"] = np.cos(df_off["theta_radian"]) * df_off["r"]
df_off["y"] = np.sin(df_off["theta_radian"]) * df_off["r"]
df_off_a = df_off.groupby("trace").apply(lambda d: sg.MultiPoint(list(zip(d["x"], d["y"]))).convex_hull.area)
fig_off = fig_off.for_each_trace(lambda t: t.update(name=f"{t.name} {df_off_a.loc[t.name]:.2f}"))

# Defensive chart
df_def = pd.concat([pd.DataFrame({"r": t.r, 
                      "theta": t.theta, 
                      "trace": np.full(len(t.r), t.name)})
        for t in fig_def.data])
df_def["theta_n"] = pd.factorize(df_def["theta"])[0]
df_def["theta_radian"] = (df_def["theta_n"] / (df_def["theta_n"].max() + 1)) * 2 * np.pi
df_def["x"] = np.cos(df_def["theta_radian"]) * df_def["r"]
df_def["y"] = np.sin(df_def["theta_radian"]) * df_def["r"]
df_def_a = df_def.groupby("trace").apply(lambda d: sg.MultiPoint(list(zip(d["x"], d["y"]))).convex_hull.area)
fig_def = fig_def.for_each_trace(lambda t: t.update(name=f"{t.name} {df_def_a.loc[t.name]:.2f}"))

# Descriptive chart
df_desc = pd.concat([pd.DataFrame({"r": t.r, 
                      "theta": t.theta, 
                      "trace": np.full(len(t.r), t.name)})
        for t in fig_desc.data])
df_desc["theta_n"] = pd.factorize(df_desc["theta"])[0]
df_desc["theta_radian"] = (df_desc["theta_n"] / (df_desc["theta_n"].max() + 1)) * 2 * np.pi
df_desc["x"] = np.cos(df_desc["theta_radian"]) * df_desc["r"]
df_desc["y"] = np.sin(df_desc["theta_radian"]) * df_desc["r"]
df_desc_a = df_desc.groupby("trace").apply(lambda d: sg.MultiPoint(list(zip(d["x"], d["y"]))).convex_hull.area)
fig_desc = fig_desc.for_each_trace(lambda t: t.update(name=f"{t.name} {df_desc_a.loc[t.name]:.2f}"))

### Getting data from the API
player_shotchart_df, league_avg = funcoes.get_player_shotchartdetail(player_name=selected_player, season_id='2022-23')



########################################################
#              Layout do corpo da página
########################################################

# st.header("👤 Single Player Vision")

# st.subheader("Player's name")
st.metric(label='',
          value=f'{selected_player}')
    # ----------------------------------------------------------------    
    
with st.container():
    col1, col2, col3, col4, col5 = st.columns([2, 5, 5, 3, 3])
    with col1:
        st.empty()
    with col2:
        # st.markdown('#### Team, Position and age')
        st.text(f'Team: {team}')
        st.text(f'Position: {position}')
        st.text(f'Jersey Number: {number}')
        st.text(f'Age: {age}')
        st.text(f'Drafted in: {draft}')
        st.text(f'Country: {country}')
        st.text(f'Height(cm): {height}')
        st.text(f'Weight(kg): {weight}')

    # ----------------------------------------------------------------    
    with col3:
        # st.empty()
        st.text(f'Games played: {games_played}')
        st.text(f'Points per game: {points}')
        st.text(f'Offensive polygon: {round(df_off_a[0], 2)}')
        st.text(f'Blocks per game: {blocks}')
        st.text(f'Defensive polygon: {round(df_def_a[0], 2)}')
        st.text(f'Plus/Minus: {round(plus_minus, 3)}')
        st.text(f'Assists per game: {assists}')
        st.text(f'Descritive polygon: {round(df_desc_a[0], 2)}')

    # ----------------------------------------------------------------    
    with col5: 
        st.empty()
        
    # ----------------------------------------------------------------    
    with col4:
        st.markdown(f"##### {selected_player}'s Shot Chart")
        plt.rcParams['figure.figsize'] = (8, 8/1.09)
        fig_shotchart = funcoes.shot_chart(player_shotchart_df, 
                                           title="{[0]}".format(player_shotchart_df['PLAYER_NAME']), 
                                           flip_court=False,
        court_lw=2)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
st.markdown("---")

# ----------------------------------------------------------------    
with st.container():
    # st.markdown('## Chart', )
    col1, col2, col3 = st.columns(3)
    # ----------------------------------------------------------------    
    with col1:
        # st.markdown('### Offensive')
        st.plotly_chart(fig_off, use_container_width=True)
        

    # ----------------------------------------------------------------    
    with col2:
        # st.markdown('### Defensive')
        st.plotly_chart(fig_def, use_container_width=True)
        
# ----------------------------------------------------------------    
    with col3:
        # st.markdown('### Other Features')
        st.plotly_chart(fig_desc, use_container_width=True)

# ----------------------------------------------------------------    

with st.container():
    st.dataframe(selected_data_complete)
