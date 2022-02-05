#!/usr/bin/env python
# coding: utf-8

# In[350]:


# Pandas and numpy for data manipulation
import numpy as np
import pandas as pd 
# Matplotlib visualization
import matplotlib.pyplot as plt
# Seaborn for visualization
import seaborn as sns


# In[351]:


df = pd.read_csv(r"C:\Users\chhok\Downloads\credit_tes.csv")


# In[352]:


# Display dataset
df


# In[353]:


# checking data type of each column
df.info()


# In[354]:


## Data Cleaning


# In[355]:


df["Months since last delinquent"].fillna("0", inplace = True)
df["Bankruptcies"].fillna("0", inplace = True)
df["Tax Liens"].fillna("0", inplace = True)
df = df.dropna(how='any',axis=0)


# In[356]:


#checking
df.info()


# In[357]:


# Statistics for each numeric column
df.describe()


# In[358]:


df


# In[359]:


plt.figure(figsize=(22,11))
sns.countplot(x='Purpose',data=df)
plt.title("Purpose of taking loan",fontdict={'fontsize':20})
plt.show()


# In[360]:


plt.figure(figsize=(8,8))
tbt = ["Stort Term", "Long Term"]
plt.pie(df.Term.value_counts(), labels = tbt, startangle = 100, explode=[0,0.09], shadow = True)
plt.title('Time Period of Taking Loan',fontdict={'fontsize':20})
plt.show()

## Short term vs long term distribution


# In[361]:


#creating variable for loan amount range
str = df["Loan Amount Categories"].value_counts()
lbr = ["100k to 500k", "500k to 1M", "above 1M", "50k to 100k", "0 to 50k"]
plt.figure(figsize=(8,8))
plt.pie(str, labels = lbr, startangle = 100)
plt.title("Loan Amount", fontdict={'fontsize':20}) 
plt.show() 


###  -- The distribution of loan amount as per amount


# In[362]:


plt.figure(figsize=(15,7))

x = df["Annual Income"]
plt.hist(x, bins=1000)
plt.xlabel("Annual Income") 
plt.ylabel("Count") 
plt.title("Income of people taking loans", fontdict={'fontsize':20}) 
plt.show()


# In[363]:


plt.figure(figsize=(15,6))
sns.countplot(x='Home Ownership',data=df)
plt.title("Home Ownership",fontdict={'fontsize':20})
plt.show()


# In[364]:


plt.figure(figsize=(15,7))

x = df["Years of Credit History"]
plt.hist(x, bins=600)
plt.xlabel("Years of Credit History") 
plt.ylabel("Count") 
plt.title("Credit History of People", fontdict={'fontsize':20}) 
plt.show()


# In[365]:


plt.figure(figsize=(15,7))

x = df["Number of Open Accounts"]
plt.hist(x, bins=200)
plt.xlabel("Number of Open Accounts") 
plt.ylabel("Count") 
plt.title("No of accounts open per person", fontdict={'fontsize':20}) 
plt.show()


# In[366]:


plt.figure(figsize=(15,7))

x = df["Credit Score"]
plt.hist(x, bins=600)
plt.xlabel("Credit Score") 
plt.ylabel("Count") 
plt.title("Credit Score of People", fontdict={'fontsize':20}) 
plt.show()


# In[367]:


plt.figure(figsize=(15,7))

x = df["Monthly Debt"]
plt.hist(x, bins=1000)
plt.xlabel("Monthly Debt") 
plt.ylabel("Count") 
plt.title("Monthly Debt Repayment", fontdict={'fontsize':20}) 
plt.show()


# In[368]:


plt.figure(figsize=(18,8))
sns.countplot(x='Years in current job',data=df)
plt.title('Job Status of people',fontdict={'fontsize':20})
plt.show()


# In[369]:


plt.figure(figsize=(18,8))
sns.countplot(x='Number of Credit Problems',data=df)
plt.title('Credit Problems',fontdict={'fontsize':20})
plt.show()


# In[370]:


df.info()


# In[371]:


df["Bankruptcies"] = df["Bankruptcies"].astype(int).astype(float)


# In[372]:


sns.pairplot(df)


# In[ ]:





# In[ ]:




