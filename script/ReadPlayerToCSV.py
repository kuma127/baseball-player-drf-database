
# coding: utf-8

import numpy as np
import pandas as pd

years = range(17,8,-1)

for year in years:
    # ウェブページから読み込み
    df = pd.read_html('https://baseball-data.com/'+"{0:02d}".format(year)+'/player/s/')

    df = df[0]
    df.set_index('No.', inplace=True)

    # カラム名の修正
    df.rename(columns={'選手名': 'Name'}, inplace=True)
    df.rename(columns={'守備': 'Position'}, inplace=True)
    df.rename(columns={'生年月日': 'Born'}, inplace=True)
    df.rename(columns={'年齢': 'Age'}, inplace=True)
    df.rename(columns={'年数': 'Years'}, inplace=True)
    df.rename(columns={'身長': 'Height'}, inplace=True)
    df.rename(columns={'体重': 'Weight'}, inplace=True)
    df.rename(columns={'血液型': 'Blood'}, inplace=True)
    df.rename(columns={'投打': 'Pi/Ba'}, inplace=True)
    df.rename(columns={'出身地': 'Place'}, inplace=True)
    df.rename(columns={'年俸(推定)': 'Salary'}, inplace=True)

    # 不要な文言を削除
    df['Age'] = df['Age'].str.replace('歳', '')
    df['Years'] = df['Years'].str.replace('年', '')
    df['Height'] = df['Height'].str.replace('cm', '')
    df['Blood'] = df['Blood'].str.replace('型', '')
    df['Weight'] = df['Weight'].str.replace('kg', '')
    df['Salary'] = df['Salary'].str.replace('万円', '')
    df['Salary'] = df['Salary'].str.replace(',', '')

    # CSVの出力
    df.to_csv('./PlayerList_Ys20'+"{0:02d}".format(year)+'.csv', encoding='utf-8')
