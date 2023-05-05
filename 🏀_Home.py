import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "🏀")


st.sidebar.markdown('# NBA PlayersDex v.0.1')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown('## Visualizing your favorite players')
st.sidebar.image('./pages/NBA_logo.png', use_column_width=True)
st.sidebar.markdown("""---""")

st.write('# NBA PlayersDex v.0.1')
st.write('## Season 22/23')

st.markdown("""
            This app is intended to give you a visual analysis of your favorite players along with a comparison of a player-to-player rank for players during season 2022 and 2023
            
            ### How to use the NBA PlayersDex
            - First tab:
                - A single player vision
            - Second tab: 
                - A player-to-player comparison
            - Third tab:
                - An overall view of the main statistics
            - Forth tab:
                - A features glossary as extracted from https://www.basketball-reference.com/
                
            ### Ask for help
                - Via Discord
                    - @piatobruno#0143
                - Via e-mail:
                    - piatobio@gmail.com
            """)