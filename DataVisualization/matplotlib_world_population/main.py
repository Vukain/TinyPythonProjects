import matplotlib.pyplot as plt
import re
al = ['1950', '2.525', '1955', '2.758',
      '1960', '3.018', '1965', '3.322', '1970', '3.682', '1975',
      '4.061', '1980', '4.440', '1985', '4.853', '1990', '5.310',
      '1995', '5.735', '2000', '6.127', '2005', '6.520', '2010',
      '6.930', '2015', '7.349']

years = [int(e) for i, e in enumerate(al) if i % 2 == 0]
pop = [float(e) for i, e in enumerate(al) if i % 2 != 0]
deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]

lines = plt.plot(years, pop, years, deaths)
# smt="--" in plot is linestyle
plt.setp(lines, color=(0.1, 0.1, 1), marker="o")
plt.grid(True)
plt.ylabel("Population in billions")
plt.xlabel("Population growth by year")
plt.title("Population growth")
plt.show()
