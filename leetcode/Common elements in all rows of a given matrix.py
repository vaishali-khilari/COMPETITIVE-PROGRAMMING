'''Common elements in all rows of a given matrix
Difficulty Level : Medium
Last Updated : 03 Jun, 2021
Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.
Example: 

Input:
mat[4][5] = {{1, 2, 1, 4, 8},
             {3, 7, 8, 5, 1},
             {8, 7, 7, 3, 1},
             {8, 1, 2, 7, 9},
            };

Output: 
1 8 or 8 1
8 and 1 are present in all rows.'''


code:-
  
def commom(mat,x,y):
  mp={}

  for i in range(y):
    mp[mat[0][i]]=1

 # print(mp)

  for i in range(1,x):
    for j in range(y):
      if mat[i][j]  in mp.keys()  and mp[mat[i][j]]==i:
        mp[mat[i][j]]=i+1

        if i==x-1:
          print(mat[i][j],end="  ")

 # print(mp)
      
mat = [[1, 2, 1, 4, 8],
  [3, 7, 8, 5, 1],
  [8, 7, 7, 3, 1],
  [8, 1, 2, 7, 9]]
x=4
y=5
print(commom(mat,x,y))
