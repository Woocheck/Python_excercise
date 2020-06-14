import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def wykresZestawienie( daneNBP, daneTrends ):
    """Zwraca notowania waluty dla danego roku"""

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    print( daneNBP.head() )
    print( daneTrends.head() )
    ax1.plot( x = daneTrends.index.values, y= daneTrends[ 'Średnia'] )
    ax1.plot( x=daneNBP.index.values, y=daneNBP[ 'usd' ] )
    ax1.legend()
    plt.xlabel("Data")
    fig.savefig('zestawienie', dpi=None, facecolor='w', edgecolor='w',\
                orientation='portrait', papertype='a4', format=None,\
                transparent=False, bbox_inches=None, pad_inches=0.1,\
                metadata=None)