arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
op=[]

for  i in range(n-k,n):
  op.append(arr[i])
for  i in range(n-k):
  op.append(arr[i])

print(op)