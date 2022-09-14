import matplotlib.pyplot as plt




#########       DATA        ##########
# first pie chart
Energies1 = 'Fuel Oil', 'Gasoil', 'Gasoline', 'LPG', 'Jet A1', 'Others'
Generation1 = [46.01, 32.97, 15.15, 2.90, 2.46, 0.505]
Colors1 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#e8f4f3']

# second pie chart
Energies2 = 'Fuel Oil', 'Gasoil', 'Gasoline', 'LPG', 'Jet A1', 'Others'
Generation2 = [46.01, 32.97, 15.15, 2.90, 2.46, 0.505]
Colors2 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#e8f4f3']

def FIGURE():
    fig = plt.figure(figsize=(12, 9))

    def figure_1():
        #fig = plt.figure(figsize=(12, 9))
        ax1 = fig.add_subplot(1, 2, 1)

        #Energies1 = 'Fuel Oil', 'Gasoil', 'Gasoline', 'LPG', 'Jet A1', 'Others'
        #Generation1 = [46.01, 32.97, 15.15, 2.90, 2.46, 0.505]
        #Colors1 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#e8f4f3']

        ax1.pie(x=Generation1,
                labels=Energies1,
                colors=Colors1,
                labeldistance=1.1, #or None
                # explode=explode1,
                autopct='%1.1f%%', # or None
                shadow=False, startangle=-0, counterclock=False, frame=False,
                # center=(1.2,1.2),
                wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        my_circle1 = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle1)

        plt.axis('equal')
        #plt.show()

    def figure_2():
        #fig = plt.figure(figsize=(12, 9))
        ax2 = fig.add_subplot(1, 2, 2)

        #Energies2 = 'Fuel Oil', 'Gasoil', 'Gasoline', 'LPG', 'Jet A1', 'Others'
        #Generation2 = [46.01, 32.97, 15.15, 2.90, 2.46, 0.505]
        #Colors2 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#e8f4f3']

        ax2.pie(x=Generation2, labels=Energies2, labeldistance=None, colors=Colors2,
                #explode=explode2,
                autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
                # center=(1.2,1.2)
                )
        my_circle2 = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle2)

        plt.axis('equal')
        plt.show()

    fig1 = figure_1()
    fig2 = figure_2()

    return fig

Figure = FIGURE()
Figure.savefig('ringtest.png', transparent=True, dpi=300)
