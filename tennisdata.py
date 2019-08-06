import datadotworld as dw
from app import db, Tournament, Player, Round, Match
import random

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

def get_tournament(t_name, ids, session) -> int:
    if t_name not in ids:
        ids[t_name] = session.query(Tournament.id).filter(Tournament.t_name==t_name).first()[0]
    return ids[t_name]
def get_round(r_name, ids, session) -> int:
    if r_name not in ids:
        ids[r_name] = session.query(Round.id).filter(Round.r_name==r_name).first()[0]
    return ids[r_name]

def get_player(last_firstinitial, player_ids, match, session) -> int:
    if last_firstinitial not in player_ids:
        last_firstinitial_list = last_firstinitial.split()
        last = last_firstinitial_list[0].title()
        first = last_firstinitial_list[1][0:1]
        result = session.query(Player.id).filter(Player.last==last, Player.first.startswith(first)).all()
        if len(result) == 0:
            player_ids[last_firstinitial] = None
            return None
        player_ids[last_firstinitial] = result[0][0]
    return player_ids[last_firstinitial]

def populate_match(matches, session):
    player_ids = dict()
    round_ids = dict()
    tournament_ids = dict()
    for match in matches:
        winner_id = get_player(match['winner'], player_ids, match, session)
        loser_id = get_player(match['loser'], player_ids, match, session)
        if not (winner_id and loser_id):
            continue
        round_id = get_round(match['round'], round_ids, session)
        tournament = get_tournament(match['tournament'], tournament_ids, session)
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