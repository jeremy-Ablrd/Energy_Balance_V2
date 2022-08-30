import matplotlib.pyplot as plt


# Create function plt.
def figure(length, width):
    plt.figure(figsize=(length, width))


def pie_chart(x, labels, colors, explode=None, label_dist=None, wedge_prop=None, text_prop=None):
    plt.axis([0, 2.4, 0, 2.4])
    plt.pie(x=x, labels=labels, colors=colors, explode=explode, labeldistance=label_dist,
            wedgeprops=wedge_prop,
            textprops=text_prop,
            autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
            center=(1.2, 1.2))


def print_text(x: float, y: float, txt: str, fontsize: int, color: str, verti_align: str, horiz_align: str, bbox=None):
    plt.text(x, y, txt, fontsize=fontsize, color=color, verticalalignment=verti_align,
             horizontalalignment=horiz_align,)

