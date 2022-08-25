import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as nd
import pandas as pd
import seaborn as sns

# -------  CHART FOR KEY FIGURE ELECTRICITY ------- #

# Read .xlsx (excel file) ; sheet_name = "Electricity Stat-2021"
path = "C:/Users/jerem/PycharmProjects/pythonProject/Infography/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Electricity Stat-2021", header=39)

# create Dataframe "df" for the table concerned [ELECTRICITY GENERATION MIX IN PUC]
df = file.iloc[0:5, 0:3]
print(df)

# Generate data parameters
energy = df['Technology'].iloc[0:4]
value_energy = df['GWh'].iloc[0:4]
share = df["Share"].iloc[0:4]
total_energy = file.iloc[4:5, 1:2]

# Change share values to percent
share_percent = []
for i in share.values:
    share_percent.append(round(i*100, 1))
share_percent = nd.array(share_percent)

# Config chart
Colors_share = ['Teal', '#42a1a1', '#ffde59', '#ff8c00']
explode = (0, 0, 0.1, 0.1)
center = (1.2, 1.2)

# Generate figure
plt.figure(figsize=(12, 9))

# Generate Pie Chart
plt.axis([0, 2.4, 0, 2.4])
plt.pie(x=value_energy, labels=energy, labeldistance=None, colors=Colors_share,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
        center=center, explode=explode)


## ------- Print ------- ##
def print_text(x: float, y: float, txt: str, fontsize: int, color: str, verti_align: str, horiz_align: str, bbox=None):
    plt.text(x, y, txt, fontsize=fontsize, color=color, verticalalignment =verti_align,
             horizontalalignment =horiz_align,)


# Call function print_text()
print_text(0.7, 1.2, str(share_percent[0]) + "%", 30, "black", 'top', 'center')
print_text(1.8, 1.55, str(share_percent[1]) + "%", 28, "black", 'top', 'center')
print_text(2.70, 1.30, str(share_percent[2]) + "%", 25, "black", 'top', 'center')
print_text(2.70, 1.48, str(share_percent[3]) + "%", 25, "black", 'top', 'center',)

plt.savefig('Electgene2020.png' ,transparent=True, dpi=300)
plt.show()


#plt.title('Store Inventory')
#plt.ylabel('Product')
#plt.xlabel('Quantity')
