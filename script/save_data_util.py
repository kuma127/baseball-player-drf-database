import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","baseball_player_drf_database.settings")
import django
django.setup()

import pandas as pd
import numpy as np
import requests
import json
import copy
from datetime import datetime as dt
from baseball_player_app.models.player import Player
from baseball_player_app.models.player_batting_stats import PlayerBattingStats
from baseball_player_app.models.player_pitching_stats import PlayerPitchingStats
from django.db.models import Max

# year: int
def save_batting_stats(url, year):
    #打者成績
    stats_df = pd.read_html(url)
    stats_df = stats_df[0]

    test_df = pd.DataFrame(index=stats_df.index, columns=[])

    test_df['no'] = stats_df['背番号']['背番号']
    test_df['name'] = stats_df['選手名']['選手名']
    test_df['avg'] = stats_df['打率']['打率']
    test_df['game'] = stats_df['試合']['試合']
    test_df['plate_appearances'] = stats_df['打席数']['打席数']
    test_df['at_bats'] = stats_df['打数']['打数']
    test_df['runs_scored'] = stats_df['得点']['得点']
    test_df['hits'] = stats_df['安打']['安打']
    test_df['two_base_hits'] = stats_df['二塁打']['二塁打']
    test_df['three_base_hits'] = stats_df['三塁打']['三塁打']
    test_df['home_runs'] = stats_df['本塁打']['本塁打']
    test_df['total_bases'] = stats_df['塁打']['塁打']
    test_df['runs_batted_in'] = stats_df['打点']['打点']
    test_df['stolen_bases'] = stats_df['盗塁']['盗塁']
    test_df['caught_stealing'] = stats_df['盗塁刺']['盗塁刺']
    test_df['sacrifice_bunts'] = stats_df['犠打']['犠打']
    test_df['sacrifice_flies'] = stats_df['犠飛']['犠飛']
    test_df['bases_on_balls'] = stats_df['四球']['四球']
    test_df['intentional_walk'] = stats_df['敬遠']['敬遠']
    test_df['hit_by_pitch'] = stats_df['死球']['死球']
    test_df['strike_outs'] = stats_df['三振']['三振']
    test_df['double_plays'] = stats_df['併殺打']['併殺打']
    test_df['on_base_percentage'] = stats_df['出塁率']['出塁率']
    test_df['slugging_percentage'] = stats_df['長打率']['長打率']

    test_df = test_df.replace('-', 0)

    test_df = test_df.astype({'avg': 'float64', 'on_base_percentage': 'float64', 'slugging_percentage': 'float64'})

    for record in test_df.itertuples():
        try:
            player = Player.objects.get(name=record.name,info_year=str(year))
        except Player.DoesNotExist:
            continue

        PlayerBattingStats.objects.update_or_create(
            player=player,
            year=year,
            avg=record.avg,
            game=record.game,
            plate_appearances=record.plate_appearances,
            at_bats=record.at_bats,
            runs_scored=record.runs_scored,
            hits=record.hits,
            two_base_hits=record.two_base_hits,
            three_base_hits=record.three_base_hits,
            home_runs=record.home_runs,
            total_bases=record.total_bases,
            runs_batted_in=record.runs_batted_in,
            stolen_bases=record.stolen_bases,
            caught_stealing=record.caught_stealing,
            sacrifice_bunts=record.sacrifice_bunts,
            sacrifice_flies=record.sacrifice_flies,
            bases_on_balls=record.bases_on_balls,
            intentional_walk=record.intentional_walk,
            hit_by_pitch=record.hit_by_pitch,
            strike_outs=record.strike_outs,
            double_plays=record.double_plays,
            on_base_percentage=record.on_base_percentage,
            slugging_percentage=record.slugging_percentage
        )

def save_pitching_stats(url, team, year):
    # 投手成績 ex.) https://baseball-data.com/18/stats/pitcher2-s/ip3-1.html
    pitch_df = pd.read_html(url)

    pitch_df = pitch_df[0]

    pitch_ex_df = pd.DataFrame(index=pitch_df.index, columns=[])

    pitch_ex_df['no'] = pitch_df['背番号']['背番号']
    pitch_ex_df['name'] = pitch_df['選手名']['選手名']
    pitch_ex_df['earned_run_average'] = pitch_df['防御率']['防御率']
    pitch_ex_df['game'] = pitch_df['試合']['試合']
    pitch_ex_df['wins'] = pitch_df['勝利']['勝利']
    pitch_ex_df['losses'] = pitch_df['敗北']['敗北']
    pitch_ex_df['saves'] = pitch_df['セlブ']['セlブ']
    pitch_ex_df['holds'] = pitch_df['ホlルド']['ホlルド']
    pitch_ex_df['hold_points'] = pitch_df['HP']['HP']
    pitch_ex_df['complete_games'] = pitch_df['完投']['完投']
    pitch_ex_df['shoutout'] = pitch_df['完封勝']['完封勝']
    pitch_ex_df['no_walks'] = pitch_df['無四球']['無四球']
    pitch_ex_df['win_percentage'] = pitch_df['勝率']['勝率']
    pitch_ex_df['batters_faced'] = pitch_df['打者']['打者']
    pitch_ex_df['innings_pitched'] = pitch_df['投球回']['投球回']
    pitch_ex_df['hits'] = pitch_df['被安打']['被安打']
    pitch_ex_df['home_runs'] = pitch_df['被本塁打']['被本塁打']
    pitch_ex_df['bases_on_balls'] = pitch_df['与四球']['与四球']
    pitch_ex_df['intentional_walk'] = pitch_df['敬遠']['敬遠']
    pitch_ex_df['hit_by_pitch'] = pitch_df['与死球']['与死球']
    pitch_ex_df['strike_outs'] = pitch_df['奪三振']['奪三振']
    pitch_ex_df['wild_pitches'] = pitch_df['暴投']['暴投']
    pitch_ex_df['balks'] = pitch_df['ボlク']['ボlク']
    pitch_ex_df['runs_allowed'] = pitch_df['失点']['失点']
    pitch_ex_df['earned_runs_allowed'] = pitch_df['自責点']['自責点']

    pitch_ex_df = pitch_ex_df.replace('-', 0)

    pitch_ex_df = pitch_ex_df.astype({'earned_run_average': 'float64', 'win_percentage': 'float64', 'innings_pitched': 'float64'})

    for record in pitch_ex_df.itertuples():
        try:
            player = Player.objects.get(name=record.name, team=team, info_year=str(year))
        except Player.DoesNotExist:
            continue

        PlayerPitchingStats.objects.update_or_create(
            player=player,
            year=year,
            earned_run_average=record.earned_run_average,
            game=record.game,
            wins=record.wins,
            losses=record.losses,
            saves=record.saves,
            holds=record.holds,
            hold_points=record.hold_points,
            complete_games=record.complete_games,
            shoutout=record.shoutout,
            no_walks=record.no_walks,
            win_percentage=record.win_percentage,
            batters_faced=record.batters_faced,
            innings_pitched=record.innings_pitched,
            hits=record.hits,
            home_runs=record.home_runs,
            bases_on_balls=record.bases_on_balls,
            intentional_walk=record.intentional_walk,
            hit_by_pitch=record.hit_by_pitch,
            strike_outs=record.strike_outs,
            wild_pitches=record.wild_pitches,
            balks=record.balks,
            runs_allowed=record.runs_allowed,
            earned_runs_allowed=record.earned_runs_allowed
        )
