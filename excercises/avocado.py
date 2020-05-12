import pandas as pd
import matplotlib.pyplot as plt

avocadoDS = pd.read_csv('https://query.data.world/s/xjgixhlxpuzocwyhznapqgynkv66gj')

print( avocadoDS.head() )

print( avocadoDS['Year'].unique() )
print( pd.crosstab( avocadoDS['Small Hass'], avocadoDS['Year']  ) )

atlantaDS = avocadoDS[ (avocadoDS['Region'] == 'Atlanta') &  (avocadoDS['Type'] == 'conventional')]

