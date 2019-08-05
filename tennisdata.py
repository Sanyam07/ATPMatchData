import datadotworld as dw
from app import db, Tournament, Player, Round, Match

def populate_player_table(players, session):
    id = 0
    for player in players:
        attributes = {
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
        

def populate_tournament_round(matches, session):
    tournaments_added = set()
    rounds_added = set()
    for match in matches:
        tournament_attributes = {
            't_name': match['tournament'],
            'location': match['location'],
            'surface': match['surface'],
            'series': match['series']
        }
        if not (tournament_attributes['t_name'] in tournaments_added):
            t = Tournament(**tournament_attributes)
            session.add(t)
            tournaments_added.add(tournament_attributes['t_name'])
        round_attributes = {
            'r_name': match['round']
        }
        if not (round_attributes['r_name'] in rounds_added):
            r = Round(**round_attributes)
            session.add(r)
            rounds_added.add(round_attributes['r_name'])

def get_tournament(t_name, session) -> int:
    return session.query(Tournament.id).filter(Tournament.t_name==t_name).first()[0]

def get_round(r_name, session) -> int:
    return session.query(Round.id).filter(Round.r_name==r_name).first()[0]

def get_player(last_firstinitial, player_ids, match, session) -> int:
    if last_firstinitial in player_ids:
        return player_ids[last_firstinitial]
    else:
        last_firstinitial = last_firstinitial.split()
        last = last_firstinitial[0]
        first = last_firstinitial[1][0:1]
        result = session.query(Player.id).filter(Player.last==last, Player.first.startswith(first)).all()
        if (len(result) != 1):
                print(last_firstinitial)
                return None
        
        return result[0][0]

def populate_match(matches, session):
    for match in matches:
        player_ids = dict()
        winner_id = get_player(match['winner'], match, session)
        loser_id = get_player(match['loser'], match, session)
        if not (winner_id and loser_id):
            continue
        round_ids = dict()
        round_id = get_round(match['round'], session)
        tournament_ids = dict()
        tournament = get_tournament(match['tournament'], session)
        match_attributes = {
            'm_date': match['match_date'],
            'best_of': match['best_of'],
            'w_set1': match['w1'],
            'l_set1': match['l1'],
            'w_set2': match['w2'],
            'l_set2': match['l2'],
            'w_set3': match['w3'],
            'l_set3': match['l3'],
            'w_set4': match['w4'],
            'l_set4': match['l4'],
            'w_set5': match['w5'],
            'l_set5': match['l5'],
            'winner_rank': match['wrank'],
            'loser_rank': match['lrank'],
            'winner': winner_id,
            'loser': loser_id,
            't_round': round_id,
            'tournament': tournament
        }
        m = Match(**match_attributes)
        session.add(m)


if __name__ == '__main__':
    session = db.session()
    lds = dw.load_dataset('tylerudite/atp-match-data')
    matches = lds.tables['atp_matches_combined']
    # players = lds.tables['atp_players']
    # populate_tournament_round(matches, session)
    # populate_player_table(players, session)
    populate_match(matches, session)
    session.commit()
    session.close()