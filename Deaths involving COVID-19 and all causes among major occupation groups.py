#!/usr/bin/env python
# coding: utf-8

# This is me creating my first line graph using Python and matplotlib. Exciting! 
# 
# So to begin with, I am going to import the package matplotlib which will create the graph and set it as a variable of plt. 
# 
# Then, I am going to input my data that I want to use. In this case, I am looking at the deaths involving COVID-19 and other causes among major occupations for men and women. 

# In[ ]:


import matplotlib.pyplot as plt
Occupation = ['Managers, directors and senior officials','Professional occupations','Assosiate professional and technical occupations','Administrative and secretarial occupations','Skilled trades occupations','Caring, leisure and other service occupations','Sales and customer service occupations','Process, plant and machine operatives','Elementary occupations']
Deaths_men = [294,277,227,125,500,160,98,473,421]
Deaths_women = [78,181,63,157,27,264,105,26,124]


# Now we have the data, we can start to plot the data and start to visualise it. So first, we are going to tell matplotlib what we want it to plot and include. 
# 
# We will then give our graph a title. Self-explanatory.
# Then, we will tell our graph what we want it to measure by, in this case we want it to be measured by the major occupations. 
# 
# As for the values, we want the values of the men and women so that it can make a comparison, so we include the variable names that we gave it above.
# 
# Then we are going to cross our fingers and hope it works by using the function plt.show()

# In[41]:


plt.plot(Occupation, Deaths_men, Deaths_women)
plt.title('Occupation of men that died of COVID-19')
plt.xlabel('Occupation')
plt.ylabel('Deaths_men''Deaths_women')
plt.show()


# Woohoo! We created our first ever graph using Python. These are some exciting times. 
# 
# However, this is just plain messy, and luckily there are ways that we can clean this up! 
# 
# So, we are simply going to copy and past the exact same code we used before, but this time we are going to include commands and instructions to make it look better and more readable! 

# In[46]:


plt.plot(Occupation, Deaths_men, "y", marker="o")
plt.plot(Occupation, Deaths_women, "b", marker="o")
plt.title('Deaths involving COVID-19 and all causes among major occupations', fontsize=1)
plt.xlabel('Occupation')
plt.ylabel('Men''Women', fontsize=10)
plt.xticks(rotation=90)
plt.show()

