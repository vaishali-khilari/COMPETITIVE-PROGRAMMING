median of two array of different size



code:-
  
def find_median(n,v):
  v.sort()
  if n%2!=0:
    return v[n//2]
  else:
    return (v[n//2]+v[(n//2)-1])//2
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

v=sorted(arr1+arr2)
n=len(v)
print(find_median(n,v))


