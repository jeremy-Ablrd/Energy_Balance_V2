from Electricity_main import *

# ------------- CONFIG DATA  ------------- #

# Config chart
colors_share = ['Teal', '#42a1a1', '#ffde59', '#ff8c00']
gap = (0, 0, 0.1, 0.1)

# ---------------- CALL FUNCTION ---------------- #

# Call function figure()
figure(12, 9)

# Call function pie_chart()
pie_chart(value_energy, energy, colors_share, gap)

# Call function print_text()
print_text(0.7, 1.2, str(share_percent[0]) + "%", 30, "black", 'top', 'center')
print_text(1.8, 1.55, str(share_percent[1]) + "%", 28, "black", 'top', 'center')
print_text(2.70, 1.30, str(share_percent[2]) + "%", 25, "black", 'top', 'center')
print_text(2.70, 1.48, str(share_percent[3]) + "%", 25, "black", 'top', 'center',)

plt.show()