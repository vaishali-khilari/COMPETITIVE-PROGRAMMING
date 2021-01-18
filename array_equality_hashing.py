def check(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    return arr1==arr2
    
if __name__ == '__main__':
  t=int(input())
  for i in  range(t):
    n=int(input())
    arr1=[int(x) for  x in input().replace('','').split()]
    arr2=[int(x) for  x in input().replace('','').split()]
    if check(arr1,arr2,n):
      print(1)
    else:
      print(0)
