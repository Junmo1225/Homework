import pandas as pd
users = pd.DataFrame({'id':[0],'name':['test'],'point':[100]})

def add_user():
    global users
    name = input('input your nickname? -> ')
    new_user = {'id':users.id.max()+1, 'name':name, 'point':100}
    print('100 point saved')

    users = users.append(new_user, ignore_index=True)

def show_user(num=10):
    print(users.head(num))
    
def add_point(name, point):
    pass
    
def save():
    users.to_csv('user.csv', index=False)
    
def load():
    global users
    users = pd.read_csv('user.csv')