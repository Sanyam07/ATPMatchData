import datadotworld as dw
from app import db, Tournament, Player, Round, Match

def populate_player_table(players, session):
    id = 0
    for player in players:
        attributes = {
            'id': id,
            'first': player['first_name'],
            'last': player['last_name'],
            'atp_url': player['player_url'],
            'country': player['flag_code'],
            'date_of_birth': player['birth_date'],
            'turned_pro': player['turned_pro'],
            'weight_lbs': player['weight_lbs'],
            'weight_kg': player['weight_kg'],
            'height_inches': player['height_inches'],
            'height_cm': player['height_cm']
        }
        try:
            attributes['handedness'] = player['handedness'][0:1]
        except:
            attributes['handedness'] = None
        try:
            attributes['backhand'] = player['backhand'][0:1]
        except:
            attributes['backhand'] = None

        session.add(Player(**attributes))
        id += 1
        

def add_tournament():
    try:
        pass
    except:
        pass

def add_round():
    try:
        pass
    except:
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
    # populate_player_table(players, session)
    populate_tournament_round_match_tables(matches, session)
    session.commit()
    session.close()