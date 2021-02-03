#!/usr/bin/env python
# coding: utf-8

# In[6]:


user_name = "Fatih"
password ="123456"

user_name1 =input("Please enter your user name")

password1= input("Please enter your password.")

if (user_name != user_name1 and password == password1):
    print("Invalid user name")
    
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")


# In[5]:


user_name = "Fatih"
password ="123456"

user_name1 =input("Please enter your user name")

password1= input("Please enter your password.")

dict_1 = {"Fatih":user_name1, "123456":password1}

if (user_name != user_name1 and password == password1):
    print("Invalid user name")
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")


# In[ ]:




