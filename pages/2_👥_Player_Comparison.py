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
selected_player_A = st.sidebar.selectbox(label='Select the player', 
                       options=data['PLAYER_NAME'].unique(),
                       index=252)
selected_data_A = data[data['PLAYER_NAME'] == selected_player_A]

selected_player_B = st.sidebar.selectbox(label='Select the player', 
                       options=data['PLAYER_NAME'].unique(),
                       index=166)
selected_data_B = data[data['PLAYER_NAME'] == selected_player_B]

selected_data_complete = data_complete[(data_complete['PLAYER_NAME']==selected_player_A) | (data_complete['PLAYER_NAME']==selected_player_B)]



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


#--------------------- FEATURE SELECTION ------------------- #
offensive_features = ['PTS', 'AST', 'FG_PCT', 'FG3_PCT', 'FT_PCT', ]
defensive_features = ['OREB', 'DREB', 'STL', 'BLK', 'CONTESTED_SHOTS', 'BOX_OUTS', 'CHARGES_DRAWN']
descriptive_features = ['GP', 'MIN', 'PF', 'PFD', 'TOV', 'REB']


# ----------------- DATA PREPARATION ------------------------- # 
# CHARTS DATA
# Offensive features
auxA_off = data[data['PLAYER_NAME'] == selected_player_A][offensive_features].T
auxA_off.columns = [selected_player_A]
auxB_off = data[data['PLAYER_NAME'] == selected_player_B][offensive_features].T
auxB_off.columns = [selected_player_B]

# Defensive features
auxA_def = data[data['PLAYER_NAME'] == selected_player_A][defensive_features].T
auxA_def.columns = [selected_player_A]
auxB_def = data[data['PLAYER_NAME'] == selected_player_B][defensive_features].T
auxB_def.columns = [selected_player_B]

# Descriptive features
auxA_desc = data[data['PLAYER_NAME'] == selected_player_A][descriptive_features].T
auxA_desc.columns = [selected_player_A]
auxB_desc = data[data['PLAYER_NAME'] == selected_player_B][descriptive_features].T
auxB_desc.columns = [selected_player_B]

# DEFINING FIGURES
# Offensive chart
fig_off = go.Figure()
fig_off.add_trace(go.Scatterpolar(
    r=auxA_off[selected_player_A],
    theta=offensive_features,
    fill='toself',
    name=selected_player_A))
fig_off.add_trace(go.Scatterpolar(
    r=auxB_off[selected_player_B],
    theta=offensive_features,
    fill='toself',
    name=selected_player_B))
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
    r=auxA_def[selected_player_A],
    theta=defensive_features,
    fill='toself',
    name=selected_player_A))
fig_def.add_trace(go.Scatterpolar(
    r=auxB_def[selected_player_B],
    theta=defensive_features,
    fill='toself',
    name=selected_player_B))
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
    r=auxA_desc[selected_player_A],
    theta=descriptive_features,
    fill='toself',
    name=selected_player_A))
fig_desc.add_trace(go.Scatterpolar(
    r=auxB_desc[selected_player_B],
    theta=descriptive_features,
    fill='toself',
    name=selected_player_B))
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


########################################################
#              Layout do corpo da página
########################################################

# ------------- HEADER -------- #
# ----------------------------- #
with st.container():
    col1, col2 = st.columns(2)
    # ------------- Left container -------- #
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
                st.text(f'Offensive polygon: {round(df_off_a[0], 2)}')

            with col4:
                st.text(f'Country: {country_A}')
                st.text(f'Height(cm): {height_A}')
                st.text(f'Weight(kg): {weight_A}')
                st.text(f'Defensive polygon: {round(df_def_a[0], 2)}')

            with col5: 
                st.text(f'Plus/Minus: {round(plus_minus_A, 3)}')
                st.text(f'Drafted in: {draft_A}')
                st.text(f'Jersey Number: {number_A}')
                st.text(f'Descritive polygon: {round(df_desc_a[0], 2)}')
    # ------------- Right container -------- #
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
                st.text(f'Offensive polygon: {round(df_off_a[1], 2)}')

            with col7:
                st.text(f'Country: {country_B}')
                st.text(f'Height(cm): {height_B}')
                st.text(f'Weight(kg): {weight_B}')
                st.text(f'Defensive polygon: {round(df_def_a[1], 2)}')

            with col8: 
                st.text(f'Plus/Minus: {round(plus_minus_B, 3)}')
                st.text(f'Drafted in: {draft_B}')
                st.text(f'Jersey Number: {number_B}') 
                st.text(f'Descritive polygon: {round(df_desc_a[1], 2)}') 
st.markdown("---")

# ------------------------------------------------------- #   
# ---------------------- BODY --------------------------- #   
# ------------------------------------------------------- #   
with st.container():
    # st.markdown('## Chart', )
    col1, col2, col3 = st.columns(3)
    
    # ---------------------- OFFENSIVE ------------------------ #   
    with col1:
        # st.markdown('### Offensive')
        st.plotly_chart(fig_off, use_container_width=True)

    # ---------------------- DEFENSIVE ------------------------ #   
    with col2:
        # st.markdown('### Defensive')
        st.plotly_chart(fig_def, use_container_width=True)

        
    # ---------------------- DESCRIPTIVE ------------------------ #   
    with col3:
        # st.markdown('### Other Features')
        st.plotly_chart(fig_desc, use_container_width=True)
# ----------------------------------------------------------------

with st.container():
    st.dataframe(selected_data_complete)