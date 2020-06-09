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


