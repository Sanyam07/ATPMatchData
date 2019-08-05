import datadotworld as dw
from app import db, Tournament, Player, Round, Match

def populate_player_table(players, session):
    id = 0
    for player in players:
        attributes = (id,
            player['first_name'],
            player['last_name'],
            player['player_url'],
            player['flag_code'],
            player['birth_date'],
            player['turned_pro'],
            player['weight_lbs'],
            player['weight_kg'],
            player['height_inches'],
            player['height_cm'],
            player['handedness'],
            player['backhand'])
        session.add(Player(*attributes))
        id += 1
        

def add_tournament():
    pass

def add_round():
    pass

def add_match():
    pass

def populate_tournament_round_match_tables(matches, session):
    pass

if __name__ == '__main__':
    session = db.session()
    lds = dw.load_dataset('tylerudite/atp-match-data')
    matches = lds.tables['atp_matches_combined']
    players = lds.tables['atp_players']
    populate_player_table(players, session)
    populate_tournament_round_match_tables(matches, session)
    session.commit()
    session.close()