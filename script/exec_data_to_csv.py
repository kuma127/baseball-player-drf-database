# データをあれこれ操作するファイル

import pandas as pd
import numpy as np
import requests
import json
import copy
from baseballdata import BaseBallData
from baseball_player_list import getPlayerURL,getLeftyList,getRightyList,getPlayerURL2017,getLeftyList2017,getRightyList2017,getPlayerURL2016,getLeftyList2016,getRightyList2016,getSwitchList,getSwitchList2016,getSwitchList2017
import time

YEAR = 2018

REST = 180

def execute():
    #player_list = getLeftyList()
    #player_list = getRightyList()
    player_list = getSwitchList()

    for key in player_list:
        try:
            url = getPlayerURL(key,YEAR)
            player = BaseBallData(url=url, year=YEAR)
            df_result = player.get_result_data()
            df_count = player.get_result_count()

            if df_result is not None and df_count is not None:
                #df_result.to_csv('./CSV/' + str(YEAR) + '/Lefty/result/' + key + '_' + str(YEAR) + '_result.csv', encoding='utf-8')
                #df_count.to_csv('./CSV/' + str(YEAR) + '/Lefty/count/' + key + '_' + str(YEAR) + '_count.csv', encoding='utf-8')
                #df_result.to_csv('./CSV/' + str(YEAR) + '/Righty/result/' + key + '_' + str(YEAR) + '_result.csv', encoding='utf-8')
                #df_count.to_csv('./CSV/' + str(YEAR) + '/Righty/count/' + key + '_' + str(YEAR) + '_count.csv', encoding='utf-8')
                df_result.to_csv('./CSV/' + str(YEAR) + '/Switch/result/' + key + '_' + str(YEAR) + '_result.csv', encoding='utf-8')
                df_count.to_csv('./CSV/' + str(YEAR) + '/Switch/count/' + key + '_' + str(YEAR) + '_count.csv', encoding='utf-8')
                print(key + ' completed!')
            else:
                print(key + ' is not found in ' + str(YEAR))

            time.sleep(REST)
        except:
            print('error! at ' + key)
            break

def execute_2017():
    #player_list = getLeftyList2017()
    #player_list = getRightyList2017()
    player_list = getSwitchList2017()

    for key in player_list:
        try:
            url = getPlayerURL2017(key)
            player = BaseBallData(url=url, year=2017)
            df_result = player.get_result_data()
            df_count = player.get_result_count()

            if df_result is not None and df_count is not None:
                #df_result.to_csv('./CSV/2017/Lefty/result/' + key + '_2017_result.csv', encoding='utf-8')
                #df_count.to_csv('./CSV/2017/Lefty/count/' + key + '_2017_count.csv', encoding='utf-8')
                #df_result.to_csv('./CSV/2017/Righty/result/' + key + '_2017_result.csv', encoding='utf-8')
                #df_count.to_csv('./CSV/2017/Righty/count/' + key + '_2017_count.csv', encoding='utf-8')
                df_result.to_csv('./CSV/2017/Switch/result/' + key + '_2017_result.csv', encoding='utf-8')
                df_count.to_csv('./CSV/2017/Switch/count/' + key + '_2017_count.csv', encoding='utf-8')
                print(key + ' completed!')
            else:
                print(key + ' is not found in 2017')

            time.sleep(REST)
        except:
            print('error! at ' + key)
            break

def execute_2016():
    #player_list = getLeftyList2016()
    player_list = getRightyList2016()
    #player_list = getSwitchList2016()

    for key in player_list:
        try:
            url = getPlayerURL2016(key)
            player = BaseBallData(url=url, year=2016)
            df_result = player.get_result_data()
            df_count = player.get_result_count()

            if df_result is not None and df_count is not None:
                #df_result.to_csv('./CSV/2016/Lefty/result/' + key + '_2016_result.csv', encoding='utf-8')
                #df_count.to_csv('./CSV/2016/Lefty/count/' + key + '_2016_count.csv', encoding='utf-8')
                df_result.to_csv('./CSV/2016/Righty/result/' + key + '_2016_result.csv', encoding='utf-8')
                df_count.to_csv('./CSV/2016/Righty/count/' + key + '_2016_count.csv', encoding='utf-8')
                #df_result.to_csv('./CSV/2016/Switch/result/' + key + '_2016_result.csv', encoding='utf-8')
                #df_count.to_csv('./CSV/2016/Switch/count/' + key + '_2016_count.csv', encoding='utf-8')
                print(key + ' completed!')
            else:
                print(key + ' is not found in 2016')

            time.sleep(REST)
        except:
            print('error! at ' + key)
            break

def only_test():
    key = 'YS_SAKAGUCHI'
    url = getPlayerURL(key,YEAR)
    player = BaseBallData(url=url, year=YEAR)
    df_result = player.get_result_data()
    df_count = player.get_result_count()

    if df_result is not None and df_count is not None:
        # df_result.to_csv('./CSV/' + str(YEAR) + '/Lefty/result/' + key + '_' + str(YEAR) + '_result.csv', encoding='utf-8')
        # df_count.to_csv('./CSV/' + str(YEAR) + '/Lefty/count/' + key + '_' + str(YEAR) + '_count.csv', encoding='utf-8')
        df_result.to_csv('./CSV/' + str(YEAR) + '/Righty/result/' + key + '_' + str(YEAR) + '_result.csv', encoding='utf-8')
        df_count.to_csv('./CSV/' + str(YEAR) + '/Righty/count/' + key + '_' + str(YEAR) + '_count.csv', encoding='utf-8')
        print(key + ' completed!')
    else:
        print(key + ' is not found in ' + str(YEAR))

# 2018,2017のみ対応
def getAllResultLefty(year):
    key_list = []
    if year == 2018:
        key_list = getLeftyList()
    elif year == 2017:
        key_list = getLeftyList2017()
    elif year == 2016:
        key_list = getLeftyList2016()
    
    df_all = pd.DataFrame(index=[], columns=[])

    for key in key_list:
        df = pd.DataFrame(index=[], columns=[])
        try:
            df = pd.read_csv('./CSV/' + str(year) + '/Lefty/count/' + key + '_' + str(year) + '_count.csv', index_col=0).rename(columns={'count' : key})
        except FileNotFoundError:
            print(key + ' is not found')
            continue
        
        df_all = pd.concat([df_all, df] , axis=1, join='outer')
    
    return df_all

# 2018,2017のみ対応
def getAllResultRighty(year):
    key_list = []
    if year == 2018:
        key_list = getRightyList()
    elif year == 2017:
        key_list = getRightyList2017()
    elif year == 2016:
        key_list = getRightyList2016()
    
    df_all = pd.DataFrame(index=[], columns=[])

    for key in key_list:
        df = pd.DataFrame(index=[], columns=[])
        try:
            df = pd.read_csv('./CSV/' + str(year) + '/Righty/count/' + key + '_' + str(year) + '_count.csv', index_col=0).rename(columns={'count' : key})
        except FileNotFoundError:
            print(key + ' is not found')
            continue
        
        df_all = pd.concat([df_all, df] , axis=1, join='outer')
    
    return df_all

# 2018,2017のみ対応
def getAllResultSwitch(year):
    key_list = []
    if year == 2018:
        key_list = getSwitchList()
    elif year == 2017:
        key_list = getSwitchList2017()
    elif year == 2016:
        key_list = getSwitchList2016()
    
    df_all = pd.DataFrame(index=[], columns=[])

    for key in key_list:
        df = pd.DataFrame(index=[], columns=[])
        try:
            df = pd.read_csv('./CSV/' + str(year) + '/Switch/count/' + key + '_' + str(year) + '_count.csv', index_col=0).rename(columns={'count' : key})
        except FileNotFoundError:
            print(key + ' is not found')
            continue
        
        df_all = pd.concat([df_all, df] , axis=1, join='outer')
    
    return df_all

def getAllResult(year):
    df_left = getAllResultLefty(year)
    df_right = getAllResultRighty(year)
    df_switch = getAllResultSwitch(year)

    df_all = pd.concat([df_left, df_right] , axis=1, join='outer')
    df_all = pd.concat([df_all, df_switch] , axis=1, join='outer')

    return df_all


if __name__ == '__main__':
    #execute()
    #execute_2017()
    execute_2016()
    #only_test()
