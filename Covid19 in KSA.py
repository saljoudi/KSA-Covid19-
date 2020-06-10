#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("path/for/your/file.csv")


# In[3]:


df.head()


# # Split Cumulative and Daily Numbers & Index Them

# In[4]:


Cumulative = (df[df["Daily / Cumulative"]=="Cumulative"])
Cumulative = Cumulative.set_index("Date")
Daily = (df[df["Daily / Cumulative"]=="Daily"])
Daily = Daily.set_index("Date")


# # Split Cumulative

# In[5]:


#'Cases', 'Recoveries', 'Mortalities', 'Active cases'
C_Active = (Cumulative[Cumulative["Indicator"]=="Active cases"])
C_Active = C_Active.iloc[:,4:]

C_Cases = (Cumulative[Cumulative["Indicator"]=="Cases"])
C_Cases = C_Cases.iloc[:,4:]

C_Recoveries = (Cumulative[Cumulative["Indicator"]=="Recoveries"])
C_Recoveries = C_Recoveries.iloc[:,4:]

C_Mortalities = (Cumulative[Cumulative["Indicator"]=="Mortalities"])
C_Mortalities = C_Mortalities.iloc[:,4:]


# # Split Daily

# In[6]:


#'Cases', 'Recoveries', 'Mortalities'

D_Cases = (Daily[Daily["Indicator"]=="Cases"])
D_Cases = D_Cases.iloc[:,4:]

D_Recoveries = (Daily[Daily["Indicator"]=="Recoveries"])
D_Recoveries = D_Recoveries.iloc[:,4:]

D_Mortalities = (Daily[Daily["Indicator"]=="Mortalities"])
D_Mortalities = D_Mortalities.iloc[:,4:]


# # Reshape Them

# In[7]:


#'Cases', 'Recoveries', 'Mortalities', 'Active cases'
C_Active = pd.DataFrame(C_Active.stack())
C_Active["C_Active"] = C_Active[0]
C_Active = C_Active.drop(columns=[0])
C_Active.index.names = ["Date","City"]

C_Cases =pd.DataFrame(C_Cases.stack())
C_Cases["C_Cases"] = C_Cases[0]
C_Cases = C_Cases.drop(columns=[0])
C_Cases.index.names = ["Date","City"]

C_Recoveries = pd.DataFrame(C_Recoveries.stack())
C_Recoveries["C_Recoveries"] = C_Recoveries[0]
C_Recoveries = C_Recoveries.drop(columns=[0])
C_Recoveries.index.names = ["Date","City"]

C_Mortalities = pd.DataFrame(C_Mortalities.stack())
C_Mortalities["C_Mortalities"] = C_Mortalities[0]
C_Mortalities.index.names = ["Date","City"]
C_Mortalities = C_Mortalities.drop(columns=[0])



#'Cases', 'Recoveries', 'Mortalities'
D_Cases =pd.DataFrame(D_Cases.stack())
D_Cases["D_Cases"] = D_Cases[0]
D_Cases = D_Cases.drop(columns=[0])
D_Cases.index.names = ["Date","City"]


D_Recoveries = pd.DataFrame(D_Recoveries.stack())
D_Recoveries["D_Recoveries"] = D_Recoveries[0]
D_Recoveries = D_Recoveries.drop(columns=[0])
D_Recoveries.index.names = ["Date","City"]


D_Mortalities = pd.DataFrame(D_Mortalities.stack())
D_Mortalities["D_Mortalities"] = D_Mortalities[0]
D_Mortalities = D_Mortalities.drop(columns=[0])
D_Mortalities.index.names = ["Date","City"]


# # Join Them

# In[8]:


Final = pd.concat([D_Recoveries, D_Cases,D_Mortalities,C_Active,C_Cases,C_Mortalities,C_Recoveries], axis=1)
Final.head()


# In[9]:


Final = Final.reset_index()
Final["Date"] = pd.to_datetime(Final["Date"])
Final2 = Final.set_index("Date")
Final2 = Final2.sum(level=0)


# In[10]:


Final2.tail()


# ### Adding Closed Cases, % Active out of Total Confirmed &  % Closed out of Total Confirmed

# In[11]:


Final2["Growth Factor"] = round(Final2["C_Active"] / Final2["C_Active"].shift(1),2)
Final2["C_Closed_cases"] = Final2["C_Recoveries"] + Final2["C_Mortalities"]
Final2["D_Closed_cases"] = Final2["D_Recoveries"] + Final2["D_Mortalities"]
Final2["Closed Out Of Total Confirmed"] = (round(Final2["C_Closed_cases"] / Final2["C_Cases"],2)) *100
Final2["Active Out Of Total Confirmed"] = (round(Final2["C_Active"] / Final2["C_Cases"],2)) *100


# In[12]:


Final2.tail()


# # Graph 1

# In[20]:


plt.figure(figsize=(15,7))
ax = sns.lineplot(Final2.index,"C_Closed_cases",data=Final2,color="green",label="Cumulative Closed cases")
ax = sns.lineplot(Final2.index,"C_Active",data=Final2,color="blue",label="Active Cases")
ax = sns.lineplot(Final2.index,"C_Cases",data=Final2,color="black",label="Cumulative Cases")
ax.set_facecolor("gray")
plt.xlabel('Date',size=12)
plt.ylabel('Number',size=12)
plt.xticks(size=10)
plt.yticks(size=10)
plt.title("Saudi Arabia as of June 8",size=15)
sns.set_style('darkgrid', {'legend.frameon':True,'grid.linestyle': u'--','figure.facecolor': 'white'})
legend = plt.legend(frameon = 1)
frame = legend.get_frame()
frame.set_color('white')
#plt.savefig(path/for/the/saved/graph.jpg")
plt.show()


# # Graph 2 

# In[21]:


plt.figure(figsize=(15,7))
ax = sns.lineplot(Final2.index,"Closed Out Of Total Confirmed",data=Final2,color="green",label="Closed out of Total Confirmed")
ax = sns.lineplot(Final2.index,"Active Out Of Total Confirmed",data=Final2,color="blue",label="Active out of Total Confirmed")
ax.set_facecolor("gray")
plt.xlabel('Date',size=12)
plt.ylabel('Percentage %',size=12)
plt.xticks(size=10)
plt.yticks(size=10)
plt.title("Saudi Arabia: Active Cases vs Closed Cases",size=15)
legend = plt.legend(frameon = 1)
frame = legend.get_frame()
frame.set_color('white')
#plt.savefig(path/for/the/saved/graph.jpg")
plt.show()


# # Graph 3

# In[22]:


plt.figure(figsize=(15,7))
ax = sns.lineplot(Final2.index,"Growth Factor",data=Final2,color="blue",label="Active Cases' Growth Factor")
ax.set_facecolor("gray")
plt.xlabel('Date',size=12)
plt.ylabel('Growth Factor',size=12)
plt.xticks(size=10)
plt.yticks(size=10)
plt.title("Saudi Arabia: Active Cases' Growth Factor",size=15)
legend = plt.legend(frameon = 1)
frame = legend.get_frame()
frame.set_color('white')
#plt.savefig(path/for/the/saved/graph.jpg")
plt.show()


# In[ ]:


plt.figure(figsize=(15,7))
ax = sns.lineplot(Final2.index,"D_Cases",data=Final2,color="blue",label="Daily New Cases")
ax = sns.lineplot(Final2.index,"D_Closed_cases",data=Final2,color="green",label="Daily Closed Cases")

ax.set_facecolor("gray")
plt.xlabel('Date',size=12)
plt.ylabel('Number',size=12)
plt.xticks(size=10)
plt.yticks(size=10)
plt.title("Saudi Arabia: Daily Closed & New Cases",size=15)
legend = plt.legend(frameon = 1)
frame = legend.get_frame()
frame.set_color('white')
#plt.savefig(path/for/the/saved/graph.jpg")
plt.show()

