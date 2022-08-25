import matplotlib.pyplot as plt
import numpy as nd
import pandas as pd

# -------  CHART FOR KEY FIGURE ELECTRICITY ------- #

# Read .xlsx (excel file) ; sheet_name = "Electricity Stat-2021"
path = "C:/Users/jerem/PycharmProjects/pythonProject/Infography/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Electricity Stat-2021", header=39)

# create Dataframe "df" for the table concerned [ELECTRICITY GENERATION MIX IN PUC]
df = file.iloc[0:5, 0:3]
print(df)

# Config data parameters
energy = df['Technology'].iloc[0:4]
value_energy = df['GWh'].iloc[0:4]
share = df["Share"].iloc[0:4]
total_energy = file.iloc[4:5, 1:2]

# Change share values to percent
share_percent = []
for i in share.values:
    share_percent.append(round(i*100, 1))
share_percent = nd.array(share_percent)


# Create function plt.
def figure(length, width):
    plt.figure(figsize=(length, width))


def pie_chart(x, labels, colors, explode):
    plt.axis([0, 2.4, 0, 2.4])
    plt.pie(x=x, labels=labels, colors=colors, explode=explode, labeldistance=None,
            autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
            center=(1.2, 1.2))


def print_text(x: float, y: float, txt: str, fontsize: int, color: str, verti_align: str, horiz_align: str, bbox=None):
    plt.text(x, y, txt, fontsize=fontsize, color=color, verticalalignment=verti_align,
             horizontalalignment=horiz_align,)


plt.show()

#plt.savefig('Electgene2021.png', transparent=True, dpi=300)
