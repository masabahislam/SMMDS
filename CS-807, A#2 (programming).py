#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing necessary library
import numpy as np


# In[2]:


#taking a full column rank matrix A
A = np.array(([1,-3],[-1,2],[1,-1],[1,2]))


# In[3]:


# P= A * ( (A(tranpose) * A)(inverse) )*(A(transpose))


# In[7]:


# P = A(transpose)      DIRECT

At = np.transpose(A)
print(At)


# In[12]:


# P = A(transpose)      INDIRECT

def transpose(A, At):

    for i in range(len(A[0])):
        for j in range(len(A)):
            At[i][j] = A[j][i]

# To store result
At = [[0 for x in range(len(A))] for y in range(len(A[0]))]

transpose(A, At)

for i in range(len(A[0])):
    for j in range(len(A)):
        print(At[i][j], " ", end='')
    print()


# In[13]:


# Performing (A(tranpose) * A)
AtA=np.matmul(At,A)
print(AtA)


# In[14]:


# Performing ((A(tranpose) * A)(inverse))

AtA_inv= np.linalg.inv(AtA)
print(AtA_inv)


# In[15]:


# Performing (A * (A(tranpose) * A)(inverse)))

P1=np.matmul(A,AtA_inv)
print(P1)


# In[17]:


#Performing P = (# Performing (A * (A(tranpose) * A)(inverse))) *A(transpose) )

P = np.matmul(P1,At)
print(P)

