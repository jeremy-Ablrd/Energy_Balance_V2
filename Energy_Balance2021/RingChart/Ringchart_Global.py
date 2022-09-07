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
from pandas import DataFrame

path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=2, index_col=0)

# Set file and pre-treatment of Dataframe, create data frame.
df = file.iloc[25:36, 0:13]
rename_columns = df.rename(columns={'Prod. (+)                 Cons. (-)': 'Electricity',
                                    'Prod. (+)                 Cons. (-).1': 'Solar Water Heater'}, inplace=True)


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
        list_series.append(value_percent(list_))
    return index_series, list_series

# change the data in percentage
def value_percent(shares: list):
    share_percent = []
    for each_share in shares:
        operation = (each_share / sum(shares)) * 100
        share_percent.append(round(operation, 2))
    return share_percent


SECTORS = ['Residential',
           # 'Service', 'Industry'
           ]
index_global, energy_global = create_data_sector(SECTORS)        # call of function
print("Index Global:", index_global)
print("Energy Sector:", energy_global)
colors = ['#52A8A8', '#A3B825', '#ffc966']

# Create figure


# create data
def chart(x, label, color=None):
    plt.figure(figsize=(12, 9))
    plt.pie(x=x, labels=label, colors=color, labeldistance=None,
            # explode=explode2,
            pctdistance=0.65,
            autopct='%2.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            textprops={'fontsize': 27, 'color': 'black'}
            # center=(1.2,1.2)
            )
    plt.show()


def simplified_dataframe(dataframe: DataFrame):
    dict_ = {}
    for i in dataframe.index:
        if i == "Solar Water Heater":
            dict_[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
        elif i == "Fuelwood & charcoal":
            dict_[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
        elif i == "Kerosene":
            dict_[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
    dict_df = pd.DataFrame(dict_).T
    somme = dict_df.iloc[:].sum(axis=0)
    # # print("Somme dictionnaire:", somme)
    # # new DataFrame
    new_df = pd.concat([dataframe, somme], axis=0)
    print(new_df)
    print(dict_df)
    print(somme)
   # return new_df




# call data in for loop
for energy, label in enumerate(index_global):
    en_sector = energy_global[energy]
    # chart(en_sector, label)
    n_df = pd.DataFrame(en_sector, columns=['Value'], index=label)
    sorted_n_df = n_df.sort_values(by='Value', ascending=False)
    print(sorted_n_df)
    simplified_dataframe(sorted_n_df)






#chart(energy_global, index_global)

    #modifier chart avec boucle for pour obtenir energy et label separement
