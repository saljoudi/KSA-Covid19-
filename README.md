## The Covid19's Situation in the Kingdom of Saudi Arabia. Facts and Insights.  
  
I have been working almost everyday in analyzing Covid19 datasets. I first statred with several countries I was interestd in seeing their situations, but then I kind of came to the relization that inside each country there are a lot different cities and regions and anayzing the whole country would bring much of insghts. Therefore, I decided to look for other datasets which have details info by cities. Finally, I came acroos dataset. This dataset usually updated daily and contains all numbers of Covid19 cases, mortalities, recoveries, and active cases by cities. It does povide other info, but I have looked at them yet.  

So, in this personal project I am going to walk you through how to handle this dataset & what insights it can offer. I mainly use data visualization tools to show the numbers and percentages. We will also answer some questions which will lead to other questions. 

#### Reminder: This is an ongoing project & should be updated daily depending on the availability of the data.  

##### Okay, let's dive in.  
**import the needed packages**  

```
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
```
**Using pandas, read the csv file.**
```
df = pd.read_csv("path/for/your/file.csv")  
df.head()
```  
The dataset looks like this:  

![I](Images/df_head.png)  

**Little info about the data.**  
The reason of doing this porocessing is that the data is mainly divided into two categories which are *Cumulative* and *Daily.*  
For each category, there are at least three sub-categories. Cumulative category contains four sub-categories which are Cases, Recoveries, Mortalities & Active cases, while Daily category contains three sub-categories which are Cases, Recoveries & Mortalities.  
There are over 150 columns in the dataset. However, there is an interesting column named Event. This columns shows the measures have been taken so far by the Saudi governemnt in their fght against Covid19. 
Further, the other columns represent cities and their numbers for categories and sub-categories.

**Next, we need to do some processings.**  
First, we need to split the two main categories. The indexing is required because we need the dates in the in the process of reshaping.
##### Splitting Cumulative and Daily Numbers & Index Them.  

```
Cumulative = (df[df["Daily / Cumulative"]=="Cumulative"])
Cumulative = Cumulative.set_index("Date")
Daily = (df[df["Daily / Cumulative"]=="Daily"])
Daily = Daily.set_index("Date")
```
##### Splitting Cumulative  
```
#'Cases', 'Recoveries', 'Mortalities', 'Active cases'
C_Active = (Cumulative[Cumulative["Indicator"]=="Active cases"])
C_Active = C_Active.iloc[:,4:]

C_Cases = (Cumulative[Cumulative["Indicator"]=="Cases"])
C_Cases = C_Cases.iloc[:,4:]

C_Recoveries = (Cumulative[Cumulative["Indicator"]=="Recoveries"])
C_Recoveries = C_Recoveries.iloc[:,4:]

C_Mortalities = (Cumulative[Cumulative["Indicator"]=="Mortalities"])
C_Mortalities = C_Mortalities.iloc[:,4:]
```
##### Splitting Daily  

```
#'Cases', 'Recoveries', 'Mortalities'

D_Cases = (Daily[Daily["Indicator"]=="Cases"])
D_Cases = D_Cases.iloc[:,4:]

D_Recoveries = (Daily[Daily["Indicator"]=="Recoveries"])
D_Recoveries = D_Recoveries.iloc[:,4:]

D_Mortalities = (Daily[Daily["Indicator"]=="Mortalities"])
D_Mortalities = D_Mortalities.iloc[:,4:]

```
In this code for example `D_Mortalities = D_Mortalities.iloc[:,4:]`, we are selecting all rows `:` from the fifth columns to the end `4:`.  
After splitting the those sup-categories, we need to reshape them and then join all these dataframes into one sngle dataframe.
I used the below to reshape the dataframes and join them into one dataframe. The reason is that I need the columns to represent the sub-categories and rows represent the dates and each city.  
```
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



#'Cases', 'Recoveries', 'Mortalities', 'Active cases'
D_Active = pd.DataFrame(D_Active.stack())
D_Active["D_Active"] = D_Active[0]
D_Active = D_Active.drop(columns=[0])
D_Active.index.names = ["Date","City"]


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
```
When we stacked the dataframes, we added another index which contains the cities' names. The second line of code basically renames the column number. The third line drops the the column which was automatically created baceuse of the stacking and named 0. The fourth line renames the indexes. Then, the process is repeated for each new category.  
Nex, we finally join the dataframes into our final one. However, this datframes contains data for each day by city. To make it r
![](Images/Join_them.png)  

 However, this datframes contains data for each day by city. To make it represent the whole country, we need to one final step. We will need to sum all rows by dates. To do that, I will the below codes.  
 ![]()
Next step is creating further columns needed in the analysis. First one is 
