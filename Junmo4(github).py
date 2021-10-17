import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
url = 'https://finance.naver.com/item/main.naver?code=065350'
raw = pd.read_html(url, encoding = 'cp949')
df = raw[4]
a = df.query('종목명 == "영업이익(억)"')
a = a.set_index('종목명')
a = a.apply(pd.to_numeric)
print(a)
b = df.query('종목명 == "당기순이익(억)"')
b = b.set_index('종목명')
b = b.apply(pd.to_numeric)
print(b)
c = df.query('종목명 == "조정영업이익(억)"')
c = c.set_index('종목명')
c = c.apply(pd.to_numeric)
print(c)