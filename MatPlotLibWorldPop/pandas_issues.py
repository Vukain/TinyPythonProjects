import matplotlib.pyplot as plt
import pandas as pd

raw_data = {'name': ['Nick', 'Panda', 'Ari', 'Valos'],
            'jan_ir': [374, 282, 232, 304],
            'feb_ir': [473, 222, 323, 121],
            'march_ir': [84, 34, 322, 122]}

df = pd.DataFrame(raw_data, columns=['name', 'jan_ir', 'feb_ir', 'march_ir'])
df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['feb_ir']

color = [(1, .4, .4), (1, .6, 1), (.3, 1, .4), (.7, .7, .2)]

plt.pie(df['total_ir'],
        labels=df['name'],
        colors=color,
        autopct='%1.1f%%')
plt.axis('equal')
plt.show()