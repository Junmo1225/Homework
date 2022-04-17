import sqlite3
import pandas as pd

con = sqlite3.connect('C:\\Users\\Junmo\\Desktop\\sqlite-tools-win32-x86-3370200\\us_covid19_daily.db')

query = '''
        select positive, recovered, death from us_covid19_daily
        '''
        
df = pd.read_sql(query, con)