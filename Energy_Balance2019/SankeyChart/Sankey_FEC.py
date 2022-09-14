import matplotlib.pyplot as plt
import numpy as np
from matplotlib.sankey import Sankey

#FIGURE
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                title="", frameon=False)


#CONFIGURATION
sankey = Sankey(ax=ax,
                scale=0.3,
                #offset=0.05,
                #head_angle=90,
                #format='%.2f',
                unit=None,
                gap=0.1,
                #trunklength=0.
                )
#### 1 SANKEY
sankey.add(flows=[1, -0.50,-0.40, -0.10 ],
           labels=['', '', '', ''],
           orientations=[0, 0, -1, 1],
           pathlengths=[0.25, 0.25, 0.35, 0.25],
           facecolor= '#ffde59',
           edgecolor='#ffde59'
           )

#### 2 SANKEY
sankey.add(flows=[0.5, 0.05, 0.2, -0.75],
           labels=['', '', '', ''],
           orientations=[0, 1, -1, 0],
           pathlengths=[0.59, 0.25, 0.25, 0.25],
           facecolor= '#ff8c00',
           edgecolor='#ff8c00',
           prior= 0,
           connect=(1,0),
           )

#### TOP SANKEY
sankey.add(flows=[0.10,-0.05,-0.05],
           labels=['', '', ''],
           orientations=[-1, 0, -1],
           pathlengths=[0.25, 0.1, 0.28],
           facecolor= '#52A8A8',
           edgecolor='#52A8A8',
           prior= 0,
           connect=(3,0),
           )

#### BOTTOM SANKEY
sankey.add(flows=[-0.2,0.4,-0.2],
           labels=['', '', ''],
           orientations=[1, 0, 0],
           pathlengths=[0.25, 0.05, 0.25],
           facecolor= '#52A8A8',
           edgecolor='#52A8A8',
           prior= 1,
           connect=(2,0),
           )

############ REGLER LE PROBLEME DE DIMENSION EN Y METTANT UN DIAGRAMME SUR UN AUTRE AXE#######


#sankey.add(flows=[-0.60, 0.45, 0.1], label='two',
 #          orientations=[-1, 0, 1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
plt.savefig('FEC_ConsumptionSankey.png', transparent=True, dpi=300)
plt.show()