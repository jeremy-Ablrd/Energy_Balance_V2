import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
# ------- BAR CHART FOR ENERGY SECTORIAL CONSUMPTION ------- #

# Read .xlsx (excel file) ; sheet_name = "Electricity Stat-2021"

path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=99)             # Already DataFrame by pandas


def dataframe_barh(df: DataFrame):
    # Rename index
    n_index = []
    for i in range(0, len(df)):
        n_index.append(i)
    df.index = n_index
    print(df)

    # Share in % values
    share_percent = []
    for i in df['Share']:
        share_percent.append(round(i*100, 1))
    share_percent = np.array(share_percent)

    # ------- Data chart parameters ------- #

    label_ = df['SECTOR'].str.lower().str.title()      # str.lower()/upper()/title() change the letter minuscule, capital...
    data_ = share_percent
    colors_ = ['#52A8A8', '#00b386', '#A3B825', '#D1C420', '#ff8c00']
    print(list(zip(label_, share_percent)))
    return label_, data_, colors_


def dataframe_transportation(df: DataFrame):
    # Rename index
    n_index = []
    for i in range(0, len(df)):
        n_index.append(i)
    df.index = n_index
    print(df)

    # Share in % values
    share_percent = []
    for i in df['TOE'][1:4]:
        operation = (i / df['TOE'][0]) * 100
        share_percent.append(round(operation, 1))
    share_percent = np.array(share_percent)

    label_ = df['SECTOR'][1:4]
    data_ = share_percent
    colors_ = ['#494f56', '#018080', '#2b489d']
    print(list(zip(label_, share_percent)))
    return label_, data_, colors_


def funct_barh(title, share, colors):
    # --------- Figure --------- #
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(111)

    # ----------- Chart ----------- #
    plt.barh(title, width=share, height=0.6, color=colors)

    # ----------- AXE CONFIGURATION ----------- #
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    ax.xaxis.set_visible(False)
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(labelsize=20, length=0)

    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    ax.grid(visible=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    ax.invert_yaxis()
    for a in ax.patches[:-1]:
        plt.text(a.get_width() - 4, a.get_y() + 0.46,
                 s=str(round((a.get_width()), 2)) + '%',
                 fontsize=15, fontweight='bold',
                 color='black')
    for a in ax.patches[4:5]:
        plt.text(a.get_width(), a.get_y() + 0.46,
                 s=str(round((a.get_width()), 2)) + '%',
                 fontsize=15, fontweight='bold',
                 color='black')
    plt.savefig('Sectorial_Consump2021.png', transparent=True, dpi=300)


def chart(value, index, color=None):
    plt.figure(figsize=(12, 9))
    plt.pie(x=value, labels=index, colors=color, labeldistance=None,
            # explode=explode2,
            pctdistance=0.85,
            autopct='%2.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
            wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
            textprops={'fontsize': 27, 'color': 'white'}
            # center=(1.2,1.2)
            )
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.axis('equal')
    path_savefig = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/RingChart"
    plt.savefig(f'{path_savefig}/RingChart_Transport_2021.png', transparent=True, dpi=300)


# Create DataFrame (manuel parameters)
dataframe = file.iloc[0:8, 0:3]
df_barh = dataframe.drop([1, 2, 3], axis=0)
df_transport = dataframe.iloc[0:4]

total = file.loc[8][0:3]

label1, data1, colors1 = dataframe_barh(df_barh)
funct_barh(label1, data1, colors1)

label2, data2, colors2 = dataframe_transportation(df_transport)
chart(data2, label2, colors2)

plt.show()
