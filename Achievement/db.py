import pandas as pd
import datetime as dt

df = pd.DataFrame({'topic':['test'], 'body':['test body'], 'target_date':[dt.datetime.now()], 'created_date':[dt.datetime.now()]})

def create(topic, body, target_date):
    global df
    new_data = {'topic':topic, 'body':body, 'target_date':target_date,
                'created_date':dt.datetime.now()}
    df = df.append(new_data, ignore_index=True)

def read():
    return df

def update(topic, body, target_date):
    global df
    select_row = df[df.topic==topic].index
    df.loc[select_row, 'body'] = body
    df.loc[select_row, 'target_date'] = target_date

def delete(topic):
    global df
    select_row = df[df.topic==topic].index
    df = df.drop(select_row)

def save():
    pass

def load():
    pass