import numpy as np
import pandas as pd

np.random.seed(42)

college={"student_id":np.random.randint(1,7,7),
"student_name":np.random.choice(["adi","aditya"],7),
"age":np.random.choice([18,22,1000],7),
"attendence":np.random.randint(75,90,7),
"internal_marks":np.random.randint(15,20,7),
"external_marks":np.random.randint(15,20,7),
"semester":np.random.choice([1,2],7),
"gender":np.random.choice(["M","F"],7),}
#TO PRINT THE DATAFRAME
df=pd.DataFrame(college)
print(df)
#TO DISPLAY SHAPE AND SIZE
shape=np.shape(df)
size=np.size(df)
print("shape is=",shape)
print("size is=",size)
#TO FIND UNIQUE VALUES IN SEMESTER COLOUMN
unique_values=df["semester"].unique()
print("unique value is=",unique_values)
#REMOVING OUTLIERS USING IQR IN AGE COLOUMN
q1=df["age"].quantile(0.25)
q3=df["age"].quantile(0.75)
iqr=q3-q1

lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr

no_outliers=df[(df["age"]>=lower_bound) and (df["age"]<=upper_bound)]
print("age without outliers")
print(no_outliers)




