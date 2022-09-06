import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

# MAKE FIGURE & AXIS
fig = plt.figure(figsize=(12,9))

######SERVICE######
Energies2 = 'Electricity','Fuel Oil','Gasoil','LPG'
Generation2 = [40.9, 33, 23.8, 2.2]
Colors2 = ['#52A8A8', '#FFEF2C','#ff8c00','#A3B825']
explode2 = (0.001, 0.01, 0.01)

# GENERATE PIE CHART
pie1 = plt.pie(x=Generation2, labels=Energies2, labeldistance=None, colors=Colors2,
        #explode=explode2,
        pctdistance=0.85,
        autopct='%1.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 27, 'color': 'black'}
        #center=(1.2,1.2)
        )

# add a circle at the center to transform it in a donut chart
my_circle2 = plt.Circle((0,0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle2)

plt.axis('equal')

# ADD A IMAGE
#logo = mpimg.imread('Tutorial.png')
#imagebox = OffsetImage(logo, zoom=0.05)
#ab = AnnotationBbox(imagebox, (0.1, 0.1))
#ax2.add_artist(ab)

#plt.grid()

#plt.draw()


#print(plt.get_fignums())
plt.savefig('RingChart_Insdustry2020.png', transparent=True, dpi=300)
plt.show()