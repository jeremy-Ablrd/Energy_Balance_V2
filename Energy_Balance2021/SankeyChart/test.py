import matplotlib.pyplot as plt
import numpy as np
from matplotlib.sankey import Sankey

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                 title="Vereinfachtes Kraftwerksmodell")
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=[1.0, -0.3, -0.1, -0.1, -0.5],
       pathlengths = [0.5,0.06,0.5,0.5,0.375],
       labels=['P$el$', 'Q$ab,vd$', 'P$vl,vd$', 'P$vl,mot$', ''],
       label='Laden',
       orientations=[0, -1, 1, 1, 0])

sankey.add(flows=[0.5, 0.1, 0.1, -0.1, -0.1, -0.1, -0.1, -0.3], fc='#37c959',
       label='Entladen',
       labels=['P$mech$', 'Q$zu,ex$', 'Q$zu,rekup$', 'P$vl,tb$', 'P$vl,gen$',                'Q$ab,tb$', 'Q$ab,rekup$', 'P$nutz$'],
       orientations=[0, -1, -1, 1, 1, -1, -1, 0], prior=0, connect=(4, 0))

sankey.add(flows=[-0.1, 0.1],
       label='Rekuperator',
       #labels=['bla'],
       orientations=[1,1],
        prior=1,
           connect=(2, 0))

diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend(loc='lower right')
plt.show()