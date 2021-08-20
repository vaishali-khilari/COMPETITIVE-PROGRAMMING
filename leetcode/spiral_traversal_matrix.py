Spirally traversing a matrix 
Medium Accuracy: 48.39% Submissions: 57963 Points: 4
Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:

Example 2:

Input:
r = 3, c = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.

Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and returns a list of integers denoting the spiral traversal of matrix. 

Expected Time Complexity: O(r*c)




class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,a,m,n): 
        
        k=0
        l=0
        ans=[]
        while k<m and l<n:
            
            
            for i in range(l,n):
                ans.append(a[k][i])
            k+=1
            
            for i in range(k,m):
                ans.append(a[i][n-1])
            n-=1
            
            if k<m:
                for i in range(n-1,l-1,-1):
                    ans.append(a[m-1][i])
                m-=1
                
            if l<n:
                for i in range(m-1,k-1,-1):
                    ans.append(a[i][l])
                l+=1
                
                
        return ans
