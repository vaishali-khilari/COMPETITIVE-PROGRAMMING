Given an array arr of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)



code:-
arr=list(map(int,input().split()))
max_so_far=arr[0]
curr_max=arr[0]

for i in range(1,len(arr)):
  
  curr_max=max(arr[i],curr_max+arr[i])
  max_so_far=max(max_so_far,curr_max)
print(max_so_far)
  

