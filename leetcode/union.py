Array:
  Find the Union and Intersection of the two sorted arrays.



Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Example 1:

Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.


code:-
 arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
union=arr1+arr2
print(set(union))
common=[]
for i in arr1:
  if i in arr2:
    common.append(i)
print(common)


