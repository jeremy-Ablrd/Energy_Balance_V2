import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

fig = plt.figure(figsize=(12,9))
ax1 = fig.add_subplot(1,2,1)

Energies1 = 'Street Lights','Gonvernment','Résidential','Industry & Commercial'
Generation1 =[0.9, 11.8, 33.6, 53.3,]
#[46.01, 32.97, 15.15, 2.90, 2.46, 0.505]

Colors1 = ['orange', '#00ff7f', '#42a1a1', '#67b3b3']
explode1 = (0.05, 0, 0, 0)

ax1.pie(x=Generation1, labels=Energies1, labeldistance=None, colors=Colors1,
        explode=explode1,
        autopct=None, shadow=False, startangle=-0, counterclock=True, frame=False,
        #center=(1.2,1.2),
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' })

plt.show()