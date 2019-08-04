import datadotworld as dw
from app import db
import pandas as pd

def populate_player_table(pandas_players):
    pandas_players['first_name'] = pd.to_string
    pandas_players['birth_date'] = pd.to_datetime(pandas_players['birth_date'], yearfirst=True).date()
    print(pandas_players.info())

def add_tournament():
    pass

def add_round():
    pass

def add_match():
    pass

def populate_tournament_round_match_tables(pandas_matches):
    pass

if __name__ == '__main__':
    #session = db.session()
    lds = dw.load_dataset('tylerudite/atp-match-data')
    pandas_matches = lds.dataframes['atp_matches_combined']
    pandas_players = lds.dataframes['atp_players']
    #
    print(pandas_matches.info())
    #
    populate_player_table(pandas_players)
    populate_tournament_round_match_tables(pandas_matches)
    #session.commit()
    #session.close()