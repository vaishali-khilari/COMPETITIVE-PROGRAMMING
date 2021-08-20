Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45] 
[27,29,37,48] 
[32,33,39,50]]
Output:
10 15 20 25 
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.
Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3 
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.
Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.




code:-
class Solution:
    def sortedMatrix(self,N,mat):
        total=N *N

        op=[]
        for i in mat:
            for j in i:
                op.append(j)
                
                
        op.sort()
        
        res=[]
        x=[]
        p=0
        q=N
        while total:
            
            for i in range(p,q):
                res.append(op[i])
                
            x.append(res)
            res=[]
            p+=N
            q+=N
            total-=N
            
            
        return  x
