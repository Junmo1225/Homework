import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

codes = ['005930','066570','065350']

info = []
for code in codes:
    url = f'https://finance.naver.com/item/main.nhn?code={code}'
    print(url)
    raw = pd.read_html(url, encoding = 'cp949')[4]
    df = raw.iloc[:,0:2]
    df = df.set_index('종목명')
    info.append(df)
    
info_df = pd.concat(info, axis=1)

def plot_info(item):
    a = info_df.query('index == @item')
    a = a.apply(pd.to_numeric)
    a = a.T
    a1 = a.index
    
    a1_name = []
    for i in a1:
        print(i.split("*")[0])
        a1_name.append(i.split("*")[0])
    a.index = a1_name
    a.plot.bar()
    return a

영업이익 = plot_info('영업이익(억)')