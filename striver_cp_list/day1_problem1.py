#striver cp_list
#day-1
#problem_1
#Sort an array of 0's 1's & 2's | Leetcode

arr=list(map(int,input().split()))
unique=list(set(arr))
print(unique)
counter=[]
for i in range(len(unique)):
  count =arr.count(unique[i])
  counter.append(count)
print(counter)
for i in range(len(unique)):
  for j in range(counter[i]):
    print(unique[i],end=" ")
    
