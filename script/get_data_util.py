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
from baseball_player_app.models.player_result import PlayerResult
from django.db.models import Max

column_data = ['AVG','B','DAJUN','DASU','DATEN','FD','GIDA','GIHI','GS','HIT','R1','R2','R3','S','SANSHIN','SC','ST','TENSA','VS','WL','HR','ICHI','KAI','OUT','QJO']
column_data_all = ['MD','QJO','VS','GS','WL','ICHI','DAJUN','AVG','DASU','HIT','HR','DATEN','FD','ST','GIDA','GIHI','SANSHIN','KAI','SC','TENSA','OUT','R1','R2','R3','B','S','RE']

result_hit = ['左本', '中本', '右本', '左３','中３','右３','左２','中２','右２','一２','二２','三２','遊２','投２','捕２','左安','中安','右安','一安','二安','三安','遊安','投安','捕安']
result_not_out = copy.copy(result_hit)
result_not_out.extend(['四球', '敬遠', '死球'])

def getdata(url, year):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    response.encoding = response.apparent_encoding
    df = pd.read_json(response.text)
    df = df[column_data_all]

    for column in column_data_all:
        df[column] = df[column].str.replace('<td>','')
        df[column] = df[column].str.replace('</td>','')
        df[column] = df[column].str.replace('</p>','')
        df[column] = df[column].str.replace("<p style='color:#222222;'>",'')
        df[column] = df[column].str.replace("<p style='color:red;font-weight:bold;'>",'')
        df[column] = df[column].str.replace("<p style='font-weight:bold;'>",'')
        df[column] = df[column].str.replace("<td style='background:#ffd700;'>",'')
        df[column] = df[column].str.replace("<td style='background:#ffff00;'>",'')
        df[column] = df[column].str.replace("<td style='background:red;'><p style='color:white;font-weight:bold;'>",'')
        df[column] = df[column].str.replace("</b>",'')
        df[column] = df[column].str.replace("</span>",'')
        df[column] = df[column].str.replace("<th>",'')
        df[column] = df[column].str.replace("</th>",'')

        # 半角スペース
        df[column] = df[column].str.replace(" ","")
        # 全角スペース
        df[column] = df[column].str.replace("　","")

    df['RE'] = df['RE'].str.replace(r"\(1\)","")
    df['RE'] = df['RE'].str.replace(r"\(2\)","")
    df['RE'] = df['RE'].str.replace(r"\(3\)","")
    df['RE'] = df['RE'].str.replace(r"\(4\)","")
    df['RE'] = df['RE'].str.replace("<bclass='red'>",'')
    df['RE'] = df['RE'].str.replace("<spanclass='red'>",'')

    df['AVG'] = df['AVG'].str.replace('.---','.000')
    df['AVG'] = df['AVG'].str.replace('-','.000')

    df = df[df.MD != '月日']

    df = df.apply(lambda x: x.str.strip()).replace('', np.nan)
    df = df.fillna(method='ffill')
    
    df['MD'] = str(year) + "/" + df['MD']
    pd.to_datetime(df['MD'])
    df = df.astype({'AVG': 'float64', 'DASU' : 'int64', 'HIT' : 'int64'})

    return df

def get_result_count(df):

    if df is None:
        return None

    grouped = df.groupby('RE')

    df_new = grouped.count().drop(column_data, axis=1)

    if (len(df_new.ix[df_new.index == '---']) > 0):
        df_new = df_new.drop(['---'])
    
    df_new.rename(columns={'MD': 'count'}, inplace=True)
    df_new.sort_values('count', ascending=False, inplace=True)
    
    return df_new

def read_csv_result(url):
    result = pd.read_csv(url)
    result.rename(columns=
        {
            'MD': 'date',
            'QJO': 'stadium',
            'VS': 'vs',
            'GS': 'result_score',
            'WL': 'win_lose',
            'ICHI': 'position',
            'DAJUN': 'order',
            'AVG': 'avg',
            'DASU': 'at_bat',
            'HIT': 'hit',
            'HR': 'hr',
            'DATEN': 'rbi',
            'FD': 'bb_hbp',
            'ST': 'stolen_bases',
            'GIDA': 'sacrifice_bunts',
            'GIHI': 'sacrifice_flies',
            'SANSHIN': 'strike_outs',
            'KAI': 'innings',
            'SC': 'middle_score',
            'TENSA': 'difference',
            'OUT': 'out_count',
            'R1': 'first_runner',
            'R2': 'second_runner',
            'R3': 'third_runner',
            'B': 'ball_count',
            'S': 'strike_count',
            'RE': 'result'
        }, 
        inplace=True)

    return result

def trans_df_to_queryset(df, player):
    for record in df.itertuples():
        PlayerResult.objects.create(
            date=dt.strptime(record.date, '%Y/%m/%d'),
            stadium=record.stadium,
            vs=record.vs,
            result_score=record.result_score,
            win_lose=record.win_lose,
            position=record.position,
            order=record.order,
            avg=record.avg,
            at_bat=record.at_bat,
            hit=record.hit,
            hr=record.hr,
            rbi=record.rbi,
            bb_hbp=record.bb_hbp,
            stolen_bases=record.stolen_bases,
            sacrifice_bunts=record.sacrifice_bunts,
            sacrifice_flies=record.sacrifice_flies,
            strike_outs=record.strike_outs,
            innings=record.innings,
            middle_score=record.middle_score,
            difference=record.difference,
            out_count=record.out_count,
            first_runner=record.first_runner,
            second_runner=record.second_runner,
            third_runner=record.third_runner,
            ball_count=record.ball_count,
            strike_count=record.strike_count,
            result=record.result,
            player=player
        )
    return

# プロ野球データFreakの選手名鑑をDataFrameとして取得
def get_player_list(url, team, year):

    # ウェブページから読み込み
    df = pd.read_html(url)

    df = df[0]

    # カラム名の修正
    df.rename(columns={'No.': 'no'}, inplace=True)
    df.rename(columns={'選手名': 'name'}, inplace=True)
    df.rename(columns={'守備': 'position'}, inplace=True)
    df.rename(columns={'生年月日': 'born'}, inplace=True)
    df.rename(columns={'年齢': 'age'}, inplace=True)
    df.rename(columns={'年数': 'years'}, inplace=True)
    df.rename(columns={'身長': 'height'}, inplace=True)
    df.rename(columns={'体重': 'weight'}, inplace=True)
    df.rename(columns={'血液型': 'blood'}, inplace=True)
    df.rename(columns={'投打': 'pi_pa'}, inplace=True)
    df.rename(columns={'出身地': 'place'}, inplace=True)
    df.rename(columns={'年俸(推定)': 'salary'}, inplace=True)

    # 新規カラム追加
    df['team'] = team
    df['info_year'] = year

    # 不要な文言を削除
    df['age'] = df['age'].str.replace('歳', '')
    df['years'] = df['years'].str.replace('年', '')
    df['height'] = df['height'].str.replace('cm', '')
    df['blood'] = df['blood'].str.replace('型', '')
    df['weight'] = df['weight'].str.replace('kg', '')
    df['salary'] = df['salary'].str.replace('万円', '')
    df['salary'] = df['salary'].str.replace(',', '')

    # データ整形
    df['born'] = df['born'].str.replace('/', '-')
    df['id'] = Player.objects.all().aggregate(Max('id'))['id__max'] + 1 + df.index

    return df