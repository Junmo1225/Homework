import pandas as pd

user = pd.DataFrame({'id':[0,1,2,3], 'user':['test','a','b','c'],'point':[1000,100,100,100]})

select_user = user.id==2
id_drop = user[select_user].index
user = user.drop(id_drop)

id_update = user[user.id==3].index
print(id_update)
user.loc[id_update,'point'] += 100


import os

swd = os.getcwd()
print("Current Directory: ". cwd)


import inspect

print(inspect.getfille(inspect.currentframe()))