import sqlalchemy as sa

engine = sa.create_engine('mysql://root:django@52.78.162.166:54643/Junmo')

con = engine.connect()

import pandas as pd

query='select * from test'
df = pd.read_sql(query, con)

query ='''
INSERT INTO `Junmo`.`test` 
    (`name`, `phone`, `email`) VALUES 
    ('Junmo2', '010123456789', 'junmo@gmail.com');
'''
con.execute(query)