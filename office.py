import numpy as np
import pandas as pd
office={"employee_id":[1,2,3,4,5,6,7],
"employee_name":["aditya","smriti","vijay","utsav","inakshi","samarth","arsh"],
"age":np.random.choice([18,22,None],7),
"salary":np.random.randint(10,20,7),
"experience":np.random.randint(5,7,7),
"department":np.random.choice(["ML","DS"],7),
"gender":np.random.choice(["Male","Female","male","M","female","F"],7),
"city":np.random.choice(["Delhi","Mumbai"],7)}
#TO PRINT DATA FRAME
df=pd.DataFrame(office)
print(df)
#TO CONVERT DATAFRAME TO CSV
df.to_csv("office.csv",index=False)
#TO READ CSV
df=pd.read_csv("office.csv")
#TO FIND NULL VALUES IN AGE
null_values=df["age"].isnull().sum()
print("Null values is age are=",null_values)
#TO CHANGE NULL VALUES TO MEAN
#df["age"].fillna(df["age"].mean(),inplace=True)
#TO PRINT UNIQUE DEPARTMENT
unique_name=df["department"].unique()
print("unique name in department=",unique_name)
#TO MAKE GENDER COLOUM CONSISTENT
df["gender"]=df["gender"].replace({'male':'Male','M':'Male','female':'Female','F':'Female'})

print(df["gender"].value_counts())

