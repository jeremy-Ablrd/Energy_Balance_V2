from Electricity_main import *
import matplotlib.pyplot as plt

# ------------- CONFIG DATA  ------------- #

# Config data
energy_key = ['Fuel Oil', energy[2], energy[3]]
value_percent = [share_percent[0] + share_percent[1], share_percent[2], share_percent[3]]
print(energy_key)

# Config pie chart
colors_share = ['Teal', '#a3b825','#fad335']
gap = (0.25, 0, 0)

# ---------------- CALL FUNCTION ---------------- #

# Call function for figure size
figure(12, 9)

# Call function pie_chart()
pie_chart(value_percent, energy_key, colors_share, gap)

# Call function print_text()
print_text(0.7, 1.2, str(value_percent[0]) + "%", 30, "black", 'top', 'center')         #Fuel oil
print_text(2.70, 1.30, str(value_percent[1]) + "%", 25, "black", 'top', 'center')       #Wind
print_text(2.70, 1.48, str(value_percent[2]) + "%", 25, "black", 'top', 'center',)      #Solar

#plt.savefig('key_figure2021.png', transparent=True, dpi=300)
plt.show()

'''#plt.plot(x,y)
#plt.axis([0, 2.4, 0, 2.4])
plt.pie(x= Electricity_Generation, labels= Energies, labeldistance=None, colors= Colors,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False, center=(1.2, 1.2), explode=explode,
        wedgeprops = {'linewidth': 1, 'edgecolor': 'white'})

#ajoue de text
plt.text(0.5,1.2,"97.1%",
         fontsize=40,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(2.4,1.4,"1.4%",
         fontsize=28,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(2.4,1.25,"1.5%",
         fontsize=28,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )'''
