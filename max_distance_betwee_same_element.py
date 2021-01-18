def maxDistance(arr, n):
    max=0
    for i in arr:
        a=arr.index(i)
        b=len(arr)-arr[::-1].index(i)-1
        c=b-a
        if c>max:
            max=c
    return max
if __name__ == '__main__':
  t=int(input())
  for i in  range(t):
    n=int(input())
    arr=list(map(int,input().split())
    print(maxDistance(arr,n))

