#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
from plotly import __version__
get_ipython().run_line_magic('matplotlib', 'inline')
print(__version__)


# In[33]:


get_ipython().system('pip install cufflinks')


# In[34]:


import cufflinks as cf


# In[35]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[36]:


init_notebook_mode(connected=True)


# In[37]:


cf.go_offline()


# In[38]:


df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())


# In[39]:


df.head()


# In[40]:


df2 = pd.DataFrame({'Category':['A','B','C'], 'Values': [32,43,50]})


# In[41]:


df


# In[43]:


df.iplot()


# In[47]:


df.iplot(kind='scatter', x='A', y='B', mode='markers', size=20)


# In[50]:


df2.iplot(kind='bar', x='Category',y='Values')


# In[53]:


df.sum().iplot(kind='bar')


# In[54]:


df.iplot(kind='box')


# In[61]:


df3=pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10],'z':[5,4,3,2,1]})


# In[62]:


df3


# In[65]:


df3.iplot(kind='surface', colorscale='rdylbu')


# In[67]:


df['A'].iplot(kind='hist', bins=25)


# In[68]:


df.iplot(kind='hist', bins=25)


# In[69]:


df[['A','B']].iplot(kind='spread')


# In[73]:


df.iplot(kind='bubble', x='A', y='C', size='C')


# In[74]:


df.scatter_matrix()


# In[ ]:




