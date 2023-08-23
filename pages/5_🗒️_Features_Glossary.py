########################################################
#              Carregando bibliotecas
########################################################

import streamlit as st



########################################################
#              Carregando dados tratados
########################################################





########################################################
#              Layout da barra lateral
########################################################

st.sidebar.image('./pages/NBA_logo_small.png', use_column_width=True)
st.sidebar.markdown('# NBA PlayersDex v.0.2')
st.sidebar.markdown('## Season 22/23')
st.sidebar.markdown("""---""")





########################################################
#              Layout do corpo da página
########################################################

st.markdown("""       

## Selected Features

### Bios

PLAYER_ID: An identification number to each player.

PLAYER_NAME: A player's name.

TEAM_ID: An identification number to each NBA team.

TEAM_ABBREVIATION: An abbreviation to the team's name.

AGE: Player's age.

PLAYER_HEIGHT_INCHES: Player's height in inches.

PLAYER_HEIGHT_CM: Player's height in centimeters.

PLAYER_WEIGHT: Player's weight in pounds .

PLAYER_WEIGHT_KG: Player's weight in kilograms.

COLLEGE: The college where the players was before coming to the NBA.

COUNTRY: The player's nationality.

DRAFT_YEAR: The year when a player was drafted or if he was undrafted.

PLAYER_LAST_NAME: Player's last name.

PLAYER_FIRST_NAME: Player's first name.

JERSEY_NUMBER: The number of a player's jersey.

POSITION: The main position where a player acts.

### Traditional stats

GP: Games played during the season.

PTS: Points per game a player made.

REB: Number of rebounds a player got per game.

AST: Number of assists a player gave per game.

G: ????

MIN: Minutes played per game.

PLUS_MINUS: The point differential when a player on floor.

PFD: Personal fouls a player drawed towards him per game.

- Offensive

FGM: Field goals made per game.

FGA: Field goals attempted per game.

FG_PCT: Field goals made percentage per game.

FG3M: Three pointers made per game.

FG3A: Three pointers attampted per game.

FG3_PCT: Three pointers made percentage per game.

FTM: Free-throws made per game.

FTA: Free-throws attempted per game.

FT_PCT: Free-throws made percentage per game.

- Defensive

OREB: Offensive rebounds per game.

DREB: Defensive rebounds per game.

STL: Stills per game.

BLK: Blocks per game.

BLKA: Block attempts per game.

- Negative Traits

TOV: Turn-overs per game.

PF: Personal fouls per game.

### Hustle stats

CONTESTED_SHOTS: Shots a player contested.

CONTESTED_SHOTS_2PT: Shots for two points a player contested.

CONTESTED_SHOTS_3PT: Shots for three points a player contested.

DEFLECTIONS: Number of deflections a player made.

CHARGES_DRAWN: Number of charges a player draw.

SCREEN_ASSISTS: Number of screen assists a player gave.

OFF_BOXOUTS: Number of times a player drawn contact with another player in order to pusue the possession due to offensive plays.

DEF_BOXOUTS: Number of times a player drawn contact with another player in order to pusue the possession due to defensive plays.

BOX_OUTS: Number of times a player drawn contact with another player in order to pusue the possession.


------

# Positions

### Guards
- SG: Shooting Guard (armador - 1)
- PG: Point Guard (ala-armador - 2) 

### Forwards
- SF: Small Forward (ala - 3)
- PF: Power Forward (ala-pivô - 4)

### Center
- C: Center (pivô - 5)
            
            """)





