Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.


Example 1:

Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
Example 2:

Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1
Explanation:
The triplet {1, 3, 6} in 
the array sums up to 10.






class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(n-2):
            j=i+1
            r=n-1
            while j<r:
                
                if A[i]+A[j]+A[r]==X:
                    return True
                elif A[i]+A[j]+A[r]<X:
                    j+=1
                else:
                    r-=1
        return False
