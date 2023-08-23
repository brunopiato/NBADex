import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏀")


st.sidebar.markdown('# NBA PlayersDex v.0.2')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown('## Visualizing your favorite players')
st.sidebar.image('./pages/NBA_logo.png', use_column_width=True)
st.sidebar.markdown("""---""")

st.write('# NBA PlayersDex v.0.2')
st.write('## Season 22/23')

st.markdown("""
            This app is intended to give you a visual analysis of your favorite players along with a comparison of a player-to-player rank for players during season 2022 and 2023.
            
            I strongly recommend you to use the dark theme (`Settings >> Theme >> Dark`) so the colors of the charts match more elegantly.
            
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
                    - A features glossary as extracted from:
                        https://www.basketball-reference.com/
                - Note that the values inside the radar charts are 
                standardized according to the maximum for each feature
                in the dataset. It means that a value of 0.3 is equivalent 
                of 30% of the maximumfor that feature, while a value of 1.0 
                is the maximum value itselt.
                - If you want to check the real values for each feature it 
                is presented at the end of the page 
            
            ### Next features to be implemented:
            - Data from previous season players
            - Team and position filters to make search easier
            -  A clustering Machine Learning algorithm to cluster players according to their stats
            
            #### Ask for help
            - Via Discord: [brunopiato](https://discordapp.com/users/438408418429239296)
            - Via e-mail: [piatobio@gmail.com](mailto:piatobio@gmail.com)
            """)
