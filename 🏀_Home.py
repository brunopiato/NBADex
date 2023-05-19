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
            This app is intended to give you a visual analysis of your favorite players along with a comparison of a player-to-player rank for players during season 2022 and 2023.
            
            I strongly recommend you to use the dark theme (`Settings >> Theme >> Dark`) so the colors of the charts match more elegantly.
            
            ### How to use the NBA PlayersDex
                - First tab:
                    - A single player vision: so you can inspect your favorite player alone.
                - Second tab: 
                    - A player-to-player comparison: making it easier to compare two different 
                    players.
                - Third tab:
                    - An overall view of the main statistics: providing some basic insights about 
                    the main stats for the season.
                - Forth tab:
                    - Features glossary as extracted from: https://www.basketball-reference.com/
                - Note that the values inside the radar charts are standardized according to the 
                maximum for each feature in the dataset. It means that a value of 0.3 is 
                equivalent to 30% of the maximum for that feature, while a value of 1.0 is the 
                maximum value itselt.
                - If you want to check the real values for each feature it is presented at the 
                end of the page.
            
            ### Next features to be implemented:
            - New characteristics and traits about the players, like height, weight, wingspan, etc
            - Data from previous season players
            - Team and position filters to make search easier
            - Some advanced analytics like
                - Polygonal area for each chart of each player
                - Clustering method to group similar players
            
            #### Ask for help
            - Via Discord: @piatobruno#0143
            - Via e-mail: piatobio@gmail.com
            """)