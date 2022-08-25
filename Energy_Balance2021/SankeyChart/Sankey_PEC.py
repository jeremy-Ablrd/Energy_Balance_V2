import matplotlib.pyplot as plt
import numpy as np
from matplotlib.sankey import Sankey

# Diagramme Sankey Primary Energy consumption

#CREATION FIGURE
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                title="", frameon=False)        #enlever le titre apres

#CONFIGURATION
sankey = Sankey(ax=ax, scale=0.15, offset=0.05, head_angle=90,
                format='%.2f', unit=None)                   #Configuration du diagramme

#CONSTRUCTION DU DIAGRAMME
sankey.add(flows=[0.96, 0.03, 0.01, -0.40, -0.04, -0.56],
           labels=['', '','', '',
                   '', ''],
           orientations=[0, 1, -1, -1, 1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
           facecolor= '#ffde59',
           edgecolor='#000000'
           )

#
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')

#### Epaisseur du texte
diagrams[0].texts[0].set_fontsize('xx-large')
diagrams[0].texts[1].set_fontsize('xx-large')
diagrams[0].texts[2].set_fontsize('xx-large')
diagrams[0].texts[3].set_fontsize('xx-large')
diagrams[0].texts[4].set_fontsize('xx-large')
diagrams[0].texts[5].set_fontsize('xx-large')

#### Couleur Diagramme
diagrams[0].texts[5].set_fontsize('xx-large')

#### Style du texte
#plt.text(0.8, 0.3, "Text", size=50,bbox=dict(boxstyle="square", facecolor='yellow', ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8)))

#Save and plot
plt.savefig('test1.png', dpi=300, format='png',transparent=True)
plt.show()