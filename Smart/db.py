import pandas as pd
import datetime as dt
import streamlit as st

class user_db():
    
    def __init__(self, file = None):
        if file is None: file = 'smart.csv'
        self.df = pd.read_csv(file, index_col=0)
        self.df = self.df.reset_index()
        
    def create(self, 프로젝트,Task,책임자,협업,일정,설명=''):
        new_data = {'프로젝트':프로젝트, 'Task':Task, '책임자':책임자,'협업':협업,'일정':일정,
                    '작성날짜':dt.datetime.now()}
        self.df = self.df.append(new_data, ignore_index=True)
        self.save()
        
    def read(self, project = '', sort =True):
        if project=='':
            if sort:
                sorted = self.df.sort_values('일정', ascending=False)
                return sorted
            else:
                return self.df
        else:
            contain1 = self.df.프로젝트.str.contains(project, case=False)
            contain2 = self.df.Task.str.contains(project, case=False)
            contain3 = self.df.책임자.str.contains(project, case=False)
            contain = contain1 | contain2 | contain3
            if sort:
                sorted = self.df[contain].sort_values('일정', ascending=False)
                return sorted
            else:
                return self.df[contain]
        
    def save(self):
        self.df.to_csv('smart.csv', index=False)
        
    def delete(self, pro = None):
        if pro is not None:
            select_row = self.df.프로젝트.isin(pro)
            st.write(select_row.index[select_row])
            self.df = self.df.drop(select_row.index[select_row])
            self.save()