import matplotlib.pyplot as plt
import pandas as pd

# Call file
# from file create DataFrame "df"
# make different data for "residential", "service", ect...
# create function for figure and ring chart
# build different figure for each sector (by call function)
# put in collection, make sure to factorize the programme.
# plt.show() at the end

# Call file
from pandas import DataFrame

path = "../Seychelles Energy Balance For 2019 - ver5.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2019", header=2, index_col=0)

# Set file and pre-treatment of Dataframe, create data frame.
df = file.iloc[25:36, 0:13]
rename_columns = df.rename(columns={'Prod. (+)                 Cons. (-)': 'Electricity',
                                    'Prod. (+)                 Cons. (-).1': 'Solar Water Heater'}, inplace=True)


# ----------------- ALL FUNCTION ----------------- #

def create_data_sector(dataframe: DataFrame, sectors: list):
    # Drop NaN rows and take only values
    index_series = []
    list_series = []
    for sector in sectors:
        series = dataframe.loc[sector].dropna(axis=0)      # delete value NaN
        index_ = [index for index in series.index]
        list_ = [values for values in series]
        index_series.append(index_)
        list_series.append(value_percent(list_))
    return index_series, list_series


def value_percent(shares: list):
    share_percent = []
    for each_share in shares:
        operation = (each_share / sum(shares)) * 100
        share_percent.append(round(operation, 2))
    return share_percent


def simplified_dataframe(dataframe: DataFrame):
    dict_kfs = {}
    dict_gas = {}
    for i in dataframe.index:
        if i in ["Gasoil", "Gasoline"]:
            dict_gas[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)
            """ La méthode "drop" ne doit pas être à l'extérieur du "if"
             sinon il va supprimer tout les éléments du dataframe
             les éléments de cette condition est supprimé parce que l'on fait une somme de ces valeurs """

        elif i in ["Solar Water Heater", "Fuelwood & charcoal", "Kerosene"]:
            dict_kfs[i] = dataframe.loc[i]
            dataframe.drop(axis=0, labels=i, inplace=True)

    if dict_gas:
        # ------- Sum of Gasoil and Gasoline ------- #
        dict_df1 = pd.DataFrame(dict_gas).T
        somme_gas = dict_df1.iloc[:].sum(axis=0)
        # make somme to a Series :
        somme_gas = pd.DataFrame(somme_gas, columns=['Sum Gas']).T
        df_gas = pd.concat([dataframe, somme_gas], join='inner')
        return df_gas

    # ------- Sum of solar, fuelwood, Kerosene ------- #
    dict_df2 = pd.DataFrame(dict_kfs).T
    somme_kfs = dict_df2.iloc[:].sum(axis=0)
    # make somme to a Series :
    somme_kfs = pd.DataFrame(somme_kfs, columns=['Sum K.F.S']).T
    df_kfs = pd.concat([dataframe, somme_kfs], join='inner')
    return df_kfs


def assign_color(dataframe: DataFrame):
    color_mapping = {
        "Electricity": "#F1C40F",
        "LPG": "#A3B825",
        "Sum K.F.S": "#5499C7",
        "Sum Gas": "#CD6155",
        "Fuel Oil": "#52BE80",
    }
    color = [color_mapping.get(i) for i in dataframe.index if i in color_mapping]
    print("Colors :", color)
    return color


def chart(value, index, color=None):
    plt.figure(figsize=(12, 9))
    plt.pie(x=value, labels=index, colors=color, labeldistance=None,
            # explode=explode2,
            pctdistance=0.85,
            autopct='%2.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
            wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
            textprops={'fontsize': 27, 'color': 'black'}
            # center=(1.2,1.2)
            )
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.axis('equal')


# ----------------- CONFIG DATA for ring chart ----------------- #

SECTORS = ['Residential', 'Service', 'Industry', ]
index_global, energy_global = create_data_sector(df, SECTORS)        # call of function

# call data in for loop
for energy, label in enumerate(index_global):
    en_sector = energy_global[energy]
    n_df = pd.DataFrame(en_sector, columns=['Value'], index=label)
    simplified_df = simplified_dataframe(n_df)
    sorted_simplified_df = simplified_df.sort_values(by=['Value'], axis=0, ascending=False)
    # PRINT DATA
    print(SECTORS[energy], "Sector :")
    print(sorted_simplified_df)
    colors = assign_color(sorted_simplified_df)
    chart(sorted_simplified_df['Value'], sorted_simplified_df.index, colors)
    plt.savefig(f'Figure_RingChart_{SECTORS[energy]}_2019.png', transparent=True, dpi=300)

plt.show()
