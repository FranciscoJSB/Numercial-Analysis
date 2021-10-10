"""How to make tridiagonal matrix"""

# Want to create the following tridiagonal matrix
# | -4  1  0  0 |
# |  1 -4  1  0 |
# |  0  1 -4  1 |
# |  0  0  1 -4 |

import numpy.linalg as la
import numpy as np

# Construct the main diagonal (Using a for loop for demonstration)
main_diagonal = []
for i in range(4):
    main_diagonal.append(-4)

# Construct the upper and lower diagonal.
# Note they have one fewer elements.
upper_diagonal = []
for i in range(3):
    upper_diagonal.append(1)
    
lower_diagonal = []
for i in range(3):
    lower_diagonal.append(1)

""" np.diag() constructs a square matrix with your entries on the diagonal
and all other entries equal to zero. If you set the second argument
to be an integer, then np.diag() will place your elements on an off
diagonal (either above or below the diagonal)."""  
#A = np.diag(main_diagonal) + np.diag(upper_diagonal, 1) + np.diag(lower_diagonal, -1)

"""If we want to solve the matrix equation 'Ax = b', we can use use 
la.inv(A) to compute the inverse of 'A' and then use np.dot() to
multiply the inverse of 'A' to 'b', i.e., np.dot(la.inv(A),b)."""

# For example, let b = [0, 1, 2, 3]
b = []
for i in range(4):
    b.append(i)

x = np.dot(la.inv(A), b)

# Convert 'x' to a list, rather than a numpy array. 
x = x.tolist()

"""In general, there faster methods for solving the equation 'Ax = b'
that do not rely on computing the inverse of A since the computation 
is usually a lot slower. But for this class, we use 'la.inv()' 
for simplicity."""

"""An alternative method to constructing the matrix A"""
n=25
# This constructs a 4x4 list (matrix) of zeros
A = [[0 for j in range(n)] for k in range(n)]

# Main diagonal.
for i in range(n):
    A[i][i] = 4
    
# Upper diagonal.
for i in range(n-1):
    A[i][i+1] = 1
    
# Lower diagonal.
for i in range(n-1):
    A[i+1][i] = 1

print(A)    
    
"""Note for 'A[i][j]', the 'i'th entry represents the row, and the 
'j'th entry represents the column."""

"""The rest of the work will be the same."""
