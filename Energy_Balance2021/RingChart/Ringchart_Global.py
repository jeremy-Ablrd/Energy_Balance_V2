import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Call file
# from file create DataFrame "df"
# make different data for "residential", "service", ect...
# create function for figure and ring chart
# build different figure for each sector (by call function)
# put in collection, make sure to factorize the programme.
# plt.show() at the end

# Call file
path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=2, index_col=0)

# Set file and pre-treatment of Dataframe, create data frame.
df = file.iloc[25:36, 0:13]
rename_columns = df.rename(columns={'Prod. (+)                 Cons. (-)': 'Electricity',
                                    'Prod. (+)                 Cons. (-).1': 'Solar Water Heater'}, inplace=True)
#print(df)


def create_data_sector(sectors: list,):
    # Drop NaN rows and take only values
    index_series = []
    list_series = []
    for sector in sectors:
        series = df.loc[sector].dropna(axis=0)
        index_ = []
        list_ = []
        for index in series.index:
            index_.append(index)
        for values in series:
            list_.append(values)
        index_series.append(index_)
        list_series.append(list_)

    return index_series, list_series


SECTORS = ['Residential', 'Service', 'Industry']
index_global, energy_global = create_data_sector(SECTORS)        # call of function
print("Index Global:", index_global)
print("Energy Sector:", energy_global)
colors = ['#52A8A8', '#A3B825', '#ffc966']

# Create figure
fig = plt.figure(figsize=(9, 12))

# create data
def chart(x, label, color):
    plt.figure(figsize=(12, 9))
    plt.pie(x=x, labels=label, colors=color, labeldistance=None,
            # explode=explode2,
            pctdistance=0.85,
            autopct='%1.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            textprops={'fontsize': 27, 'color': 'black'}
            # center=(1.2,1.2)
            )
    plt.show()

    #modifier chart avec boucle for pour obtenir energy et label separement
chart(energy_global, index_global, colors)
for i in range(0, len(index_global)):
    label_residential = index_global[i]
    print("Sector", i+1, ':', str(label_residential))

