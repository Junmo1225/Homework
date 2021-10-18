import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
url = 'https://finance.naver.com/item/main.naver?code=065350'
raw = pd.read_html(url, encoding = 'cp949')
df = raw[4]
a = df.query('종목명 == "영업이익(억)"')
a = a.set_index('종목명')
a = a.apply(pd.to_numeric)
a = a.T
a1 = a.index
a1_name = []
for i in a1:
    print(i.split("*")[0])
    a1_name.append(i.split("*")[0])
a.index = a1_name
print(a)
a.plot.bar()
b = df.query('종목명 == "당기순이익(억)"')
b = b.set_index('종목명')
b = b.apply(pd.to_numeric)
b = b.T
b1 = b.index
b1_name = []
for i in b1:
    print(i.split("*")[0])
    b1_name.append(i.split("*")[0])
b.index = b1_name
print(b)
b.plot.bar()
c = df.query('종목명 == "조정영업이익(억)"')
c = c.set_index('종목명')
c = c.apply(pd.to_numeric)
c = c.T
c1 = c.index
c1_name = []
for i in c1:
    print(i.split("*")[0])
    c1_name.append(i.split("*")[0])
c.index = c1_name
print(c)
c.plot.bar()