def repeated(i):
  op=[]
  while i!=0:
    d=i%10
    if d in  op:
      return 0
    else:
      op.append(d)
      i=i//10
  return 1


def calculate(l,r):
  ans=0
  for x in range(l,r+1):
    ans=ans+repeated(x)
  return ans
l=int(input())
r=int(input())

print(calculate(l,r))


