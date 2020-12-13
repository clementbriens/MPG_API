# MPG_API
Unofficial Python client for the Mon Petit Gazon API


## Installation

`git clone https://github.com/clementbriens/MPG_API`

`cd MPG_API`

`virtualenv env -p python3 && source env/bin/activate`

`pip install -r requirements.txt`


## Authentication

To authenticate, initialize the MPG_API object with your email and password to your MPG account to get started.

`mpg = MPG_API('example@gmail.com', 'p455w0rd')`

## Endpoints

Each of these endpoints require the `LEAGUE_ID` parameter, which you can get from the URL when visiting your league on MPG.


### Get Wall

Get wall comments.

`mpg.get_wall(LEAGUE_ID)`

### Get Coach

Get your current XI, opponent's current XI, bonuses left, etc.

`mpg.get_coach(LEAGUE_ID)`

### Get Current Matchday

Get the current scores and fixtures.

`mpg.get_current_matchday(LEAGUE_ID)`

### Get Matchday

Get results and scores from a specific matchday (integer, [1-18]).

`mpg.get_matchday(LEAGUE_ID, MATCHDAY)`

### Get Rankings

Get the current rankings for the league.

`mpg.get_rankings(LEAGUE_ID)`

### Get Top Scorers

Get the top scorers in the league.

`mpg.get_rankings_scorer(LEAGUE_ID)`

### Get Player rankings

Get the player rankings (with/without) bonus from the league.

`mpg.get_rankings_player(LEAGUE_ID)`

### Get Team rankings

Get the team rankings from the league.

`mpg.get_rankings_team(LEAGUE_ID)`

### Get Winners

Get the league winners and prizes. NOTE: Will only display data once the league is over.

`mpg.get_rankings_winner(LEAGUE_ID)`

### Get Squads/Teams

Get the squads for every player in the league, with prices bought, etc.

`mpg.get_teams(LEAGUE_ID)`
