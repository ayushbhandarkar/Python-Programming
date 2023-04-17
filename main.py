import random

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1,50,25).reshape(5,5))
#print(" Dataframe : \n", df)

print(" Type of data-aframe : \n", type(df))
print(" \nTop rows : \n", df.head(3))
print(" \nBottom rows : \n", df.tail(2))




