import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏀")


st.sidebar.markdown('# NBA-Dex v0.2')
st.sidebar.markdown('## Season 2022-23')
st.sidebar.markdown(
    '## Visualizing your favorite players for better decision making.')
st.sidebar.image('./pages/NBA_logo.png', use_column_width=True)
st.sidebar.markdown("""---""")

st.write('# NBA PlayersDex v.0.2')
st.write('## Season 22/23')

st.markdown("""
            This app is intended to give you a visual analysis of your favorite players along with a comparison of a player-to-player rank for players during season 2022 and 2023.
            
            In each player's page you find information about that player, such as their weight, height nationality, etc, along with some charts about their stats. You'll find a
            general metric of the area of the polygons formed in the radar charts shown along with the general player's infos. The polygons are assumed to represent the overall 
            quality of the player so the measure of its area is a numerical metric to assess such information and its .
            
            ### How to use the NBA PlayersDex
                - First tab:
                    - A single player vision, with their main stats along with a shot chart and 
                    three radar charts.
                - Second tab: 
                    - A player-to-player comparison with their main stats with three comparative 
                    radar chart.
                - Third tab:
                    - Two players shot charts comparison.
                - Forth tab:
                    - An overall view of the main statistics and season analytics.
                - Fifth tabe:
                    - A features glossary as extracted from:
                        https://www.nba.com/stats/help/glossary
                        
                - Note that the values inside the radar charts are standardized according to the 
                maximum for each feature in the dataset. It means that a value of 0.3 is 
                equivalent of 30% of the maximum for that feature, while a value of 1.0 is the 
                maximum value itself.
                
                - You can check the absolute values for each feature at the end of each page.
            
            ### Next features to be implemented:
            - Data from previous season players
            - Team and position filters to make search easier
            -  A clustering Machine Learning algorithm to cluster players according to their stats
            
            #### Ask for help
            - Via Discord: [brunopiato](https://discordapp.com/users/438408418429239296)
            - Via e-mail: [piatobio@gmail.com](mailto:piatobio@gmail.com)
            """)
