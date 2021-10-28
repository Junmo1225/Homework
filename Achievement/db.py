import pandas as pd #pandas 다운로드
import datetime as dt #datetime 다운로드

df = pd.DataFrame({'topic':['test'], 'body':['test body'], 'target_date':[dt.datetime.now()], 'created_date':[dt.datetime.now()]})

def create(topic, body, target_date):
    global df #df 연결하기
    new_data = {'topic':topic, 'body':body, 'target_date':target_date,
                'created_date':dt.datetime.now()} #data 새로 만들기
    df = df.append(new_data, ignore_index=True) #새로 만든 것 df에 저장

def read():
    return df #df 가져오기

def update(topic, body, target_date):
    global df
    select_row = df[df.topic==topic].index
    df.loc[select_row, 'body'] = body #새로 다시 저장
    df.loc[select_row, 'target_date'] = target_date #새로 다시 저장

def delete(topic):
    global df #df 연결하기
    select_row = df[df.topic==topic].index
    df = df.drop(select_row) #없애기

def save():
    pass #스킵

def load():
    pass #스킵
