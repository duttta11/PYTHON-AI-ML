import pandas as pd
 import numpy as np
 np.random.seed(42)
d={
  "cgpa":np.random.randint(1,5,20),
  "marks":np.random.randint(1,100,20),
  "height":np.random.randint(130,180,20),
  "fees_lakhs":np.random.randint(10,50,20),}
df=pd.DataFrame(d)
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
mm=MinMaxScaler()
scaled_data=pd.DataFrame(mm.fit_transform(df[["cgpa","marks","height","fees_lakhs"]]))
print(scaled_data)
ss=StandardScaler()
scaled_data=pd.DataFrame(mm.fit_transform(df[["cgpa","marks","height","fees_lakhs"]]))
print(scaled_data)
