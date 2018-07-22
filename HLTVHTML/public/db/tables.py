from flask_table import Table, Col


class Results(Table):
    event = Col('Event')
    maps = Col('Maps')
    team1 = Col('Team 1')
    team1result = Col('Score')
    team2 = Col('Team 2')
    team2result = Col('Score')
