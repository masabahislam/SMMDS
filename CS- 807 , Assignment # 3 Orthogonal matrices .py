#!/usr/bin/env python
# coding: utf-8

# # Input Orthogonal Matrix Q

# In[4]:


Q = [[0,1,0],
     [-1,0,0],
     [0,0,1]]


# # Q(transpose)

# In[5]:


def transpose(Q, Qt):

    for i in range(len(Q[0])):
        for j in range(len(Q)):
            Qt[i][j] = Q[j][i]

# To store result

Qt = [[0 for x in range(len(Q))] for y in range(len(Q[0]))]

transpose(Q, Qt)

for i in range(len(Q[0])):
    for j in range(len(Q)):
        print(Qt[i][j], " ", end='')
    print()


# # Q*Q(Transpose)

# In[6]:


def matrix_multiplication(Q, Qt):
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                R[i][j] += Q[i][k] * Qt[k][j]

    for i in range(0, 3):
        for j in range(0,3 ):
            print(R[i][j], end =" ")
        print("\n", end ="")

        
R = [[0 for x in range(len(Q))] for y in range(len(Q[0]))]

matrix_multiplication(Q, Qt)


# # Q(Inverse)

# In[7]:


import math

def getMinorIndex(matrixLocal, x, y):
  minor = []
  for i in range(3):
    minorRow = []
    if i == x:
      continue
    for j in range(3):
      if j == y:
        continue
      minorRow.append(matrixLocal[i][j])
    minor.append(minorRow)
  return minor

def getDeterminant2By2(matrixLocal):
  determinant = matrixLocal[0][0] * matrixLocal[1][1] - matrixLocal[0][1] * matrixLocal[1][0]
  return determinant

def getDeterminant(matrixLocal):
  determinant = 0
  for x in range(3):
    t = getDeterminant2By2(getMinorIndex(matrixLocal, 0, x))
    e = matrixLocal[0][x]
    determinant += (t * e * math.pow(-1, x))
  return determinant

def getCofactorMatrix(matrixLocal):
  cofactorMatrix = []
  for i in range(3):
    row = []
    for j in range(3):
      e = matrixLocal[i][j]
      t = getDeterminant2By2(getMinorIndex(matrixLocal, i, j))
      row.append(t * math.pow(-1, i + j))
    cofactorMatrix.append(row)
  return cofactorMatrix

def transpose(matrixLocal):
  transposeMatrix = []
  for i in range(3):
    row = []
    for j in range(3):
      e = matrixLocal[j][i]
      row.append(e)
    transposeMatrix.append(row)
  return transposeMatrix

def divideMatrix(matrixLocal, divisor):
  ansMatrix = []
  for i in range(3):
    row = []
    for j in range(3):
      e = matrixLocal[i][j]/divisor
      row.append(e)
    ansMatrix.append(row)
  return ansMatrix

cofactor = getCofactorMatrix(Q)
adjoint = transpose(cofactor)
det = getDeterminant(Q)
QI = divideMatrix(adjoint, det)


# # Q* Q(Inverse)

# In[8]:


def matrix_multiplication(Q, QI):
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                R[i][j] += Q[i][k] * QI[k][j]

    for i in range(0, 3):
        for j in range(0,3 ):
            print(R[i][j], end =" ")
        print("\n", end ="")

R = [[0 for x in range(len(Q))] for y in range(len(Q[0]))]

matrix_multiplication(Q, QI)


# In[11]:


if Qt==QI:
    print("The inverse of an orthogonal matrix is its transpose.")
else:
    print("Not applicable.")


# In[ ]:




