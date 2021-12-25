#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Statements Assessment Test
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[23]:


st = 'Print only the words that start with s in this sentence'
mystring = st.split()
length=len(mystring)
length
mystring[0][0]
for x in mystring:
    print(mystring)


# In[28]:


#Code here
mystring = st.split()
p = []
y=0
for x in mystring:
    if mystring[y][0]=='s':
        p.append(mystring[y])
    y+=1
print(p)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[32]:


#Code Here
for x in range(0,11):
    if x%2==0:
        print(x)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[37]:


#Code in this cell
[x for x in range(1,51) if x%3==0]


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[57]:


st = 'Print every word in this sentence that has an even number of letters'


# In[59]:


#Code in this cell
mystring1 = st.split()
y=0
p1=[]
for x in mystring:
    if len(mystring1[y])%2!=0:
        p1.append(mystring1[y])
    else:
        p1.append('even!')
    y+=1
p1


# In[ ]:


[p1.append]


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[67]:


#Code in this cell
y=0
p2=[]
for x in range(1,101):
    if x%15==0:
        p2.append('FizzBuzz')
    elif x%5==0:
        p2.append('Buzz')
    elif x%3==0:
        p2.append('Fizz')
    else:
        p2.append(x)
p2


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[74]:


st = 'Create a list of the first letters of every word in this string'


# In[77]:


#Code in this cell
mystring3=st.split()
y=0
p3=[]
for x in mystring3:
    p3.append(mystring3[y][0])
    y+=1
p3


# ### Great Job!
