import pandas as pd
import matplotlib.pyplot as plt

avocadoDS = pd.read_csv('https://query.data.world/s/xjgixhlxpuzocwyhznapqgynkv66gj')

print( avocadoDS.head() )

print( avocadoDS['Year'].unique() )