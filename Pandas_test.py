import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')
iris.species.count()

iris.query('species=="setosa"')

select = 'setosa'
iris.query('species==@select')

iris.query('sepal_length>=5')

iris.query('sepal_length>=5 & species == "setosa"')
iris.query('sepal_length>=5 and species == "setosa"')

iris.query('sepal_length>=5 | species == "setosa"')
iris.query('sepal_length>=5 or species == "setosa"')

num = 5
iris.query('sepal_length>=@num')

type('num')

length = 5
width = 0.3
iris.query('sepal_length>@length and petal_width>=@width')

def select_species(species=None):
    if species is None:
        return iris
    else:
        return iris.query('species==@species')

select_species('setosa')
select_species()