import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
alive = titanic.query('alive=="yes"')
dead = titanic.query('alive=="no"')

dead_man = titanic.query('alive=="no" and sex=="male"')