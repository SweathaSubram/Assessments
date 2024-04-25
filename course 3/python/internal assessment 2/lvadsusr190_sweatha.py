# -*- coding: utf-8 -*-
"""LVADSUSR190_Sweatha.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cRA8INyan9OW_ftHFFtbDjG8kALK99gj
"""

#1.

import numpy as np
import pandas as pd
a = np.array([1,2,3,4,5,6])
print("Sum = ",a.sum())
print("Minimum = ",a.min())
print("Maximum = ",a.max())
print("Standard Deviation = ",a.std())
print("Mean = ",a.mean())

#2.
health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3
sum_h,sum_w,sum_a = 0,0,0
for i in health_data:
  sum_h += i[0]
  sum_w += i[1]
  sum_a += i[2]
mean_h =sum_h/3
mean_w = sum_w/3
mean_a = sum_a/3

for i in health_data:
  i[0]/=mean_h
  i[1]/=mean_w
  i[2]/=mean_a
print(health_data)

#3.

b = np.array([[50,60,70,80],[56,-1,98,56],[56,74,23,-1]])

for i in b:
  for j in i:
    if j==-1:
      j=np.nan
j=1
for i in b:
  print("Student ",j)
  print(np.nanmean(i[-1:-4:-1]))
  j+=1

#4.
temp_sensor = np.linspace(15,25,24)
print(temp_sensor)

#5.
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5

print("Moving Averages")
for i in range(0,len(daily_closing_prices)-window_size+1):
  print(daily_closing_prices[i:i+window_size])
  small = np.array(daily_closing_prices[i:i+window_size])
  print(np.mean(small))

#6.
c = np.array([[50,60],[56,23]])
for i in c:
  sum_h += i[0]
  sum_w += i[1]
mean_h =sum_h/3
mean_w = sum_w/3
for i in c:
  i[0]/=mean_h
  i[1]/=mean_w

print(c)

#7.
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
print(np.linalg.det(properties_matrix))

#8.
d = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(d[d>5])

#9.
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}
d =pd.DataFrame(data)
print(d)

filtered = pd.DataFrame(d[d['Age']<45], columns = ['Name','City'])
print(filtered)

#10.
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}
data = pd.DataFrame(data)
grouped = data.groupby(['Salesperson','Department']).aggregate({"Sales":"mean"})
print(grouped.sort_values(by = "Sales",ascending = False).reset_index())

#11.
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}
d = pd.DataFrame(data)
filtered_d = pd.DataFrame(d[d["Category"]=='Fruit'])
print(filtered_d)

#12.
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

# Dataset of employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}
ef = pd.DataFrame(employee_data)
pf = pd.DataFrame(project_data)
print(pd.merge(ef,pf,on = 'Employee',how = 'left'))

#13.
g = pd.read_csv('/content/Q13_sports_team_stats.csv')

grouped_g = g.groupby("TeamID").aggregate({"Wins":"mean"})
grouped_g.columns = ['Average scores']
print(grouped_g.reset_index())

#14.
h =pd.read_csv('/content/Q14_customer_purchases.csv')
#print(h)
grouped_h = h.groupby("CustomerID").aggregate({"PurchaseAmount":"sum"})
grouped_h.columns = ['Total Purchase Amount']
print(grouped_h.reset_index())

#15.
m =pd.read_csv('/content/Q15_student_grades.csv')
#print(m)

grouped_m = m.groupby("Subject").aggregate({"Grade":['min','max']})
grouped_m.columns = ['Minimum Grade','Maximum Grade']
print(grouped_m.reset_index())