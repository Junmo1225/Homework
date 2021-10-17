import pandas as pd
url = 'https://finance.naver.com/item/main.naver?code=065350'
raw = pd.read_html(url, encoding = 'cp949')
df = raw[4]
revenue = df.query('종목명 == "매출액(억)"')
revenue = revenue.set_index('종목명')
revenue.dtypes
revenue = revenue.apply(pd.to_numeric)
revenue.dtypes
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
rev_T = revenue.T
rev_T.plot.bar()
comp = rev_T.index
comp_name = []
for i in comp:
    print(i.split("*")[0])
    comp_name.append(i.split("*")[0])
rev_T.index = comp_name
rev_T.plot.bar()

rev2 = raw[3]
rev2.columns = rev2.columns.get_level_values(1)
rev2 = rev2.set_index('주요재무정보')
rev2 = rev2.T
rev2['매출액'].plot.bar()
abcd = df
abcd.set_index('영업이익(억)')