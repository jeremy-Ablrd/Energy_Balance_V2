import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import StrMethodFormatter

####      DATASET     #####
label = ['Transport', 'Service', 'Residential' , 'Industry', 'Agriculture\n& fishing']
data = [39.7, 27.9, 16.8, 13.6, 1.9]
Colors = ['#52A8A8','#00b386','#A3B825','#D1C420','#ff8c00']

####      FIGURE      #####
fig= plt.figure(figsize=(12, 4))
ax = fig.add_subplot(111)

####      BARPLOT     #####
plt.barh(label, width=data, height=0.6, color=Colors)

####      AXE CONFIGURATION     #####
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

#plt.xlabel("Courses offered")
#plt.ylabel("No. of students enrolled")

ax.xaxis.set_visible(False)
ax.xaxis.set_ticks_position('top')
ax.tick_params(labelsize=20, length=0)
#ax.yaxis.set_ticks_position('none')

ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

ax.grid(b=True, color='grey',
        linestyle='-.', linewidth=0.5,
        alpha=0.2)

ax.invert_yaxis()
for i in ax.patches[:-1]:
    plt.text(i.get_width() - 5.5, i.get_y() + 0.5,
             s=str(round((i.get_width()), 2)) + '%',
             fontsize=20, fontweight='bold',
             color='black')

plt.text(2.7,3.9,"1.9%",
         fontsize=20,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None,
         fontweight='bold'
        )

plt.tight_layout()
ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

#plt.title("Students enrolled in different courses")
plt.savefig('test_barh.png', transparent=True, dpi=300)
plt.show()