#!/usr/bin/env python
# coding: utf-8

# In[3]:


list_list=[1,2,3,4,5,6,7,8,9,10,11,12]
first_list=list_list[0:6:1]
second_list=list_list[6:12:1]
print(first_list)
print(second_list)
second_list.extend(first_list)
print(second_list)


# In[25]:


giris=int(input("Enter a single digit integer to a variable: " ))
for i in range(0,giris+2,2):
    if i> giris:
        break
    else:
    
        print(i)


# In[ ]:





# In[ ]:




