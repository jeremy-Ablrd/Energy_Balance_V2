import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------- BAR CHART FOR ENERGY SECTORIAL CONSUMPTION ------- #

# Read .xlsx (excel file) ; sheet_name = "Electricity Stat-2021"
path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2020/Seychelles Energy Balance For 2020 - ver2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2020", header=98)             # Already DataFrame by pandas

# Create DataFrame (manuel parameters)
dataframe = file.iloc[0:8, 0:3]
df = dataframe.drop([1, 2, 3], axis=0)
total = file.loc[8][0:3]

# Rename index
n_index = []
for i in range(0, len(df)):
    n_index.append(i)
df.index = n_index
print(df)

total_TOE = total['TOE']
total_share = total['Share']

# Share in % values
share_percent = []
for i in df['Share']:
    share_percent.append(round(i*100, 1))
share_percent = np.array(share_percent)


# print("Total TOE :", total_TOE, "TOE")
# print("Total %:", total_share, "%")

# ------- Data chart parameters ------- #

label = df['SECTOR'].str.lower().str.title()      # str.lower()/upper()/title() change the letter minuscule, capital...
data = share_percent
Colors = ['#52A8A8', '#00b386', '#A3B825', '#D1C420', '#ff8c00']

print(list(zip(label, share_percent)))

# --------- Figure --------- #

fig = plt.figure(figsize=(20, 4))
ax = fig.add_subplot(111)
#
# ####      BARPLOT     #####
plt.barh(label, width=data, height=0.6, color=Colors)

# ####      AXE CONFIGURATION     #####
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# plt.xlabel("Courses offered")
# plt.ylabel("No. of students enrolled")

ax.xaxis.set_visible(False)
ax.xaxis.set_ticks_position('top')
ax.tick_params(labelsize=15, length=0)
# ax.yaxis.set_ticks_position('none')

ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

ax.grid(visible=True, color='grey',
        linestyle='-.', linewidth=0.5,
        alpha=0.2)

ax.invert_yaxis()
for i in ax.patches[:-1]:
    plt.text(i.get_width() - 3, i.get_y() + 0.46,
             s=str(round((i.get_width()), 2)) + '%',
             fontsize=15, fontweight='bold',
             color='black')
for i in ax.patches[4:5]:
    plt.text(i.get_width() - 2.1, i.get_y() + 0.46,
             s=str(round((i.get_width()), 2)) + '%',
             fontsize=15, fontweight='bold',
             color='black')

plt.savefig('Sectorial_Consump2020.png', transparent=True, dpi=300)
plt.show()
