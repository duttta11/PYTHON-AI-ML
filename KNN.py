import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)
d1={"Gender":np.random.choice(["M","F"],5000),
    "Disease":np.random.choice(["yes","no"],5000)}#1 for disease and 0 for no disease
df=pd.DataFrame(d1)
print(df)

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df

le = LabelEncoder()
df['Disease'] = le.fit_transform(df['Disease'])
df

X = df[['Gender']]
y = df[['Disease']]
X,y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
y_test
y_pred

accuracy_score(y_test, y_pred)
precision_score(y_test, y_pred)
recall_score(y_test, y_pred)
f1_score(y_test, y_pred)
