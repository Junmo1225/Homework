import pandas as pd
import datetime as dt

class user_db():
    
    def __init__(self, file = None):
        if file is None:
            file = "EasyPlanner.csv"
        self.df = pd.read_csv(file, index_col = 0)
        self.df = self.df.reset_index()
        
    def create(self, pro, tsk, main, end, shrd='', desc=''):
        new_data = {'Project':pro, 'Task':tsk, "Main":main,
                    'Shared':shrd, 'End_Date':end, 
                    'Description':desc,
                    'Created_Date':dt.datetime.now()}
    