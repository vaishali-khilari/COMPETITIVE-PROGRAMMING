#A boy lost the password of his super locker. He remembers the number of digits N as well as the sum S of all the digits of his password. He know that his password is the largest number of N digits that can be possible with given sum S. As he is busy doing his homework, help him retrieving his password.


#Example 1:

#Input:
#N = 5, S = 12
#Output:
#93000
#Explanation:
#Sum of elements is 12.
#Largest possible 5 digit number is 93000.
#Example 2:

#Input:
#N = 3, S = 29
#Output:
#-1
#Explanation:
#There is no such three digit
#number whose sum is 29.

#Your Task : 
#You don't need to read input or print anything. Your task is to complete the function largestNumber() which takes 2 Integers N, and S as input parameters and returns the largest possible string, return -1 otherwise.


#Constraints:
#1 <= N <= 104
#0 <= S <= 106


#Expected Time Complexity : O(N)
#Expected Auxilliary Space : O(1)

def largestNum(n,s):
    :param n: length of given numberr
    :param s: sum of digits of number
    :return: Integer
    '''
    # code here
    num=[9,8,7,6,5,4,3,2,1,0]

    x=[]
    g=s
    for i in num:
        while i<=g and len(x)<n+1:
            x.append(i)
            g=g-i
        
    
    string=""
    for i in x[:n]:
        string=string+str(i)
    if sum(x[:n])!=s:
        return -1
    else:
        return int(string)
 if __name__='__main__':
 Testcases=int(input())
  for _ in range(Testcases):
    n,s=map(int,input().split())
    print(largestNum(n,s))
        