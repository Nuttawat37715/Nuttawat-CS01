from numpy import random
import numpy as np

x = random.randint(100, size=(5, 10))
NewRan = np.sort(x)

print(NewRan)