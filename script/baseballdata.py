"""BaseBallData
データを楽しむプロ野球の全打席成績から
データを抽出するクラス
"""

from .get_data_util import getdata, get_result_count, result_hit, result_not_out

class BaseBallData:

    def __init__(self, url, year):
        self.url = url
        self.year = year
        self.result = getdata(url, year)
        self.result_count = get_result_count(self.result)

    def get_result_data(self):
        return self.result
    
    def get_result_count(self):
        return self.result_count

    def get_result_hit(self):
        df = self.result_count
        if df is None:
            return None

        df_hit = df[df.index.isin(result_hit)]

        return df_hit

    def get_result_out(self):
        df = self.result_count
        if df is None:
            return None

        df_out = df[df.index.isin(result_not_out) == False]

        return df_out
    