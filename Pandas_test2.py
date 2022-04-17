import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
alive = titanic.query('alive=="yes"')

len(titanic)
len(alive)

alive_female = titanic.query('alive=="yes" & sex=="female"')
alive_male = titanic.query('alive=="yes" & sex=="male"')