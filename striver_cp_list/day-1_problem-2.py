#Find the Missing and Repeating Number 




n=int(input())
arr=list(map(int,input().split()))
arr1=list(set(arr))
A=sum(arr)-sum(arr1)
print("repetiting number is",A)
sum2=n*(n+1)//2
sum1=sum(arr)
B=sum2-sum1
missing_one=A+B
print("missing_number",missing_one)

