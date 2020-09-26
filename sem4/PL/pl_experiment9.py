#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\mtcars.csv')
x2=x1['mpg']
plt.hist(x2,bins=5,edgecolor='black')


# In[11]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\mtcars.csv')
x2=x1['mpg']
x3=x1['wt']
plt.scatter(x2,x3,s=100,edgecolor='black')


# In[17]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
x2=x1['customerID']
print(len(x2[x2.duplicated()]))


# In[20]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
x2=x1['TotalCharges']
print(x2.isnull().sum())


# In[21]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
print(x1['MonthlyCharges'].mean())


# In[23]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
c = 0
for i in x1['Dependents']:
    if(i=='1@#'):
        c+=1
print(c)


# In[24]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
print(x1['tenure'].dtypes)


# In[28]:


import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
x1['tenure'].replace(to_replace='Four',value=4,inplace=True)
x1['tenure'].replace(to_replace='One',value=1)


# In[29]:


x1['tenure'].where(x1['tenure']!='One',1)


# In[31]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
x1=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\churn.csv')
a=np.array(x1['tenure'])
np.where(a=='One',1,a)


# In[36]:


d=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\olympics.csv')
print(d['0'][1])


# In[37]:


f = max(d['2'])
print(f)
print(d[d['2']==f])


# In[38]:


import pandas as pd
import numpy as mp
d=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\olympics.csv')
a=np.array(d['2'][1:147],dtype='int32')
b=np.array(d['7'][1:147],dtype='int32')
c=[]
for i in range(len(a)):
    if(a[i]>b[i]):
        c.append(a[i]-b[i])
    else:
        c.append(b[i]-a[i])
m = max(c)
print(d['0'][c.index(m)+1])


# In[39]:


import pandas as pd
import numpy as mp
d=pd.read_csv('C:\\Users\\Acer\\Desktop\\juptyer nb\\olympics.csv')
a=np.array(d['2'][1:147],dtype='int32')
b=np.array(d['7'][1:147],dtype='int32')
c=[]
t=[]
for i in range(len(a)):
    t.append(a[i]+b[i])
    if(a[i]>=1 and b[i]>=1):
        if(a[i]>b[i]):
            c.append(a[i]-b[i])
        else:
            c.append(b[i]-a[i])
    else:
        c.append(0)
for i in range(len(t)):
    c.insert(i,t[i]-c[i])
m = max(c)
print(d['0'][c.index(m)+1])


# In[41]:


def add_col():
    a=np.array(d['2'][1:147],dtype='int32')
    b=np.array(d['3'][1:147],dtype='int32')
    c=np.array(d['4'][1:147],dtype='int32')
    a1=np.array(d['7'][1:147],dtype='int32')
    b1=np.array(d['8'][1:147],dtype='int32')
    c1=np.array(d['9'][1:147],dtype='int32')
    a2=np.array(d['12'][1:147],dtype='int32')
    b2=np.array(d['13'][1:147],dtype='int32')
    c2=np.array(d['14'][1:147],dtype='int32')
    p,t=[0],0
    for i in range(len(a)):
        p.append(a[i]*3+b[i]*2+c[i]+a1[i]*3+b1[i]*2+c1[i]+a2[i]*3+b2[i]*2+c2[i])
        t+=p[i]
    p.append(t)
    #d['Points']=p
    Points=pd.Series(p)
    return Points
d['Points']=add_col()
d


# In[ ]:




