import datadotworld as dw

lds = dw.load_dataset('tylerudite/atp-match-data')
pandas_matches = lds.dataframes['atp_matches_combined']
pandas_players = lds.dataframes['atp_players']

if __name__ == '__main__':
    pass