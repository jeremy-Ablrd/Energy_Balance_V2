# library
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

# MAKE FIGURE & AXIS
fig = plt.figure(figsize=(12,9))

######SERVICE######
Energies2 = 'Road Transport','Maritime Transport','Air Transport'
Generation2 = [87.5, 8.18, 4.33]
Colors2 = ['#494f56', '#018080', '#2b489d']
explode2 = (0.001, 0.01, 0.01)

# GENERATE PIE CHART
pie1 = plt.pie(x=Generation2, labels=Energies2, labeldistance=None, colors=Colors2,
        #explode=explode2,
        pctdistance=0.85,
        autopct='%1.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 27, 'color': 'white'}
        #center=(1.2,1.2)
        )

# add a circle at the center to transform it in a donut chart
my_circle2=plt.Circle((0,0), 0.7, color='#c7d0d8')
p=plt.gcf()
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
plt.savefig('RingChart_Transport2020.png', transparent=True, dpi=300)
plt.show()