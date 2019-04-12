
# coding: utf-8

# In[46]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad # модуль для интегрирования
import scipy.fftpack
import numpy.fft 
import numpy as np


# In[25]:


fixed_df = pd.read_csv("123.csv", header=None)

# fixed_df[0] = fixed_df[0].astype(float)
# fixed_df[1] = fixed_df[1].astype(float)
# fixed_df


# In[26]:


x = fixed_df[0].values.tolist()
y = fixed_df[1].values.tolist()


# In[28]:


# plt.figure()
# plt.plot(x, y, label="data")
# plt.grid(True)
# plt.show()

# fixed_df.plot()
x = list(map(float, x))
y = list(map(float, y))


# In[35]:


plt.figure(figsize=(18, 16))
plt.plot(x, y, label="data")
plt.grid(True)
plt.show()


# In[47]:


# y_fft = np.fft.fftshift(np.fft.fft(y).real)
y_fft = scipy.fftpack.fft(y)


# In[48]:


plt.figure(figsize=(18, 16))
plt.plot(h, label="data")
plt.grid(True)
plt.show()


# In[41]:


h=np.fft.irfft(y)


# In[42]:


plt.figure(figsize=(18, 16))
plt.plot(h, label="data")
plt.grid(True)
plt.show()

