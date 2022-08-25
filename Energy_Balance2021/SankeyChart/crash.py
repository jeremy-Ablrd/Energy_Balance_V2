import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.sankey import Sankey

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                title='')        #enlever le titre apres
sankey = Sankey(ax=ax, scale=0.3, offset=0.1, head_angle=90,
                format='%.2f', unit=None)                   #Configuration du diagramme
sankey.add(flows=[0.97, 0.03, -0.44, -0.56],
           labels=['Import      ', 'stock change', 'Intern bunker (Air & Marine)', 'PEC'],
           orientations=[0, 1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25],
           facecolor= '#37c959')
diagrams = sankey.finish()
plt.show()