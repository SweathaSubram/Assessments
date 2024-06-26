# -*- coding: utf-8 -*-
"""LVADSUSR190_PA_FA_Clustering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lgz7hP_459vpWvI9yWaqQPvcWWm5VIu9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv('/content/customer_segmentation.csv')
df.head()

df.shape

df.describe(include="all").T

df.isnull().sum()
#24 null values in income

df['Income'] = df["Income"].fillna(df['Income'].mean())
df.isnull().sum()

df.duplicated().sum()
#zero duplicates

#Outliers
for column in df.select_dtypes(include="number"):
  sns.boxplot(df[column])
  plt.show()

for column in df.select_dtypes(include="number"):
  q1 = df[column].quantile(0.25)
  q3 = df[column].quantile(0.75)
  iqr = q3-q1
  lower = q1 - 1.5*iqr
  upper = q3 + 1.5*iqr
  df[column] = df[column].clip(lower=lower,upper=upper)
  sns.boxplot(df[column])
  plt.show()

for column in df.select_dtypes(include="number"):
  sns.histplot(df[column])
  plt.show()

for column in df.select_dtypes(include="object"):
  df[column].value_counts().plot(kind = "bar")
  plt.show()

cor = df.select_dtypes(include="number").corr()
print("Correlation matrix")
print(cor)
sns.heatmap(cor, annot=True, fmt=".2f",cmap = "coolwarm")
plt.show()

df.columns

features = ['Income', 'Kidhome','Teenhome','Recency','NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
       'Complain']

scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

sse  = []
k_range = range(1,11)
for k in k_range:
  km = KMeans(n_clusters = k)
  km.fit(df[features])
  sse.append(km.inertia_)
plt.plot(k_range,sse)
plt.show()

km = KMeans(n_clusters = 3)
sc = silhouette_score(df[features],km.fit_predict(df[features]))
print(sc)

km = KMeans(n_clusters = 3)
pred = km.fit_predict(df[features])
df['cluster'] = pred

df.head()

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Recency,df1.Income,color = 'red')
plt.scatter(df2['Recency'],df2['Income'],color = 'yellow')
plt.scatter(df3['Recency'],df3['Income'],color = 'orange')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color = "black", marker="X",label = "centroid")
plt.legend()
plt.show()
print("cluster centers")
print(km.cluster_centers_)

df['cluster'] = df['cluster'].replace(0,"Low spending customer")
df['cluster'] = df['cluster'].replace(1,"Moderate spending customer")
df['cluster'] = df['cluster'].replace(2,"High spending customer")
df.head(20)