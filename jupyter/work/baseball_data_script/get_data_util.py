# キャッシュ化しましょう
# 目的に合わせてゴロとか打球方向別とかにマージすべき
import pandas as pd
import numpy as np
import requests
import json
import copy

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