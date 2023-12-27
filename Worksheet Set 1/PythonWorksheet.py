#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input('Enter the number'))
def rec_fact (n):
    if n == 1:
        return n
    elif n < 1:
        return ('Factorial of negative number does not exist')
    else:
        return n*rec_fact (n-1)
print (rec_fact (n))


# In[2]:


num = int(input('Enter any number :'))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a PRIME number, it is a COMPOSITE number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither Prime NOR Composite number")
else:
    print()


# In[4]:


a=input("Enter string:")
if(a==a[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")


# In[5]:


import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# In[6]:


string =input("Enter string:")
freq_dict={}
for i in string: 
    if i in freq_dict: 
        freq_dict[i]=freq_dict[i] + 1
    else: 
        freq_dict[i] = 1
        print ("Characters with their frequencies:\n",freq_dict)


# In[ ]:




