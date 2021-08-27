'''Rotate a matrix by 90 degree in clockwise direction without using any extra space
Difficulty Level : Medium
Last Updated : 11 Jun, 2021
Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

Examples: 

Input:
1 2 3 
4 5 6
7 8 9  
Output:
7 4 1 
8 5 2
9 6 3

Input:
1 2
3 4
Output:
3 1
4 2 
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Method 1

Approach: The approach is similar to Inplace rotate square matrix by 90 degrees | Set 1. The only thing that is different is to print the elements of the cycle in a clockwise direction i.e. An N x N matrix will have floor(N/2) square cycles. 
For example, a 3 X 3 matrix will have 1 cycle. The cycle is formed by its 1st row, last column, last row, and 1st column. 
For each square cycle, we swap the elements involved with the corresponding cell in the matrix in the clockwise direction. We just need a temporary variable for this.

Explanation:


'''
code:-
  
def rotate(A):

  for i in range(x):
    for j in range(x-1,-1,-1):
      print(A[j][i],end=" ")
    print()

A = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
x=len(A[0])

print(rotate(A))
