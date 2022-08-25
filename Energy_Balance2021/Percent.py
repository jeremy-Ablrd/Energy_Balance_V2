import numpy as np
import math

Transportation = {'Mahe': 354.28, 'Praslin': 46.06}
Total = sum(Transportation.values())

for key,value in Transportation.items():
    sum = (value / Total) * 100
    print(key,':',round(sum,2),'%')

print(Total)