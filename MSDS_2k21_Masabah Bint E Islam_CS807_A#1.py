#!/usr/bin/env python
# coding: utf-8

# # Gaussain Elimination (Coverting matrix to Row-Echelon-Form)

# # 1. Input Module

# In[ ]:


#importing required libraries.
import numpy as n


# In[ ]:


#Taking user input for number of rows and columns in the testing matrix.
no_of_rows = int(input("Please enter number of rows in the matrix : "))
no_of_cols = int(input("Please enter number of cols in the matrix : "))


# In[ ]:


#Initializing the matrix. 
test_matrix = []


# In[ ]:


#Getting values of the matrix by user input.
print("\n Please enter values of the matrix: ")
for rows in range(no_of_rows):
    row_entry=[]
    for cols in range(no_of_cols):
        row_entry.append(int(input("Rows:{} Cols:{} \n".format(rows+1, cols+1))))
    test_matrix.append(row_entry)


# # 2.Show Test Matrix.

# In[ ]:


for rows in range(no_of_rows):
    for cols in range(no_of_cols):
        print("\n The input matrix is: ")
        print(n.matrix(test_matrix))
        break
    break


# # 3. Function for Row-Echelon-Form operation.

# In[ ]:


#Function to covert test matrix into row echelon form.
def row_echelon_form(matrix):
    for a in range(min(len(matrix), len(matrix[0]))):
        
    #Every iteration,ignore one more row and column
        for b in range(a, len(matrix)):
            
            # Finding the first row with a non-zero value in first column/pivot.
            zeroth_row = matrix[b][a] == 0
            if zeroth_row:
                continue
            
            #Trading current row with first row since first pivot point is zero.
            matrix[a], matrix[b] = matrix[b], matrix[a]
            
            # Computing values to add to rows below for the first column to be zero.
            rowandcol_1 = matrix[a][a]
            
            for rowss in range(a + 1, len(matrix)):
                row_wise = matrix[rowss][a]
                value_changer = -1 * row_wise / rowandcol_1
                
                for colss in range(a, len(matrix[0])):
                    matrix[rowss][colss] += matrix[a][colss] * value_changer
            break
            
    #Printing out the row echelon form of test matrix.        
    print("\n The matrix after row echelon operation is :")
    print(n.matrix(matrix))


# # 4. Assigning test matrix for reduction to Row-Echelon-Form.

# In[ ]:


row_echelon_form(test_matrix)

