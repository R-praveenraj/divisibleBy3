# Given a number in the form of an array A of size N. 
#Each of the digits of the number is represented by A[i]. Check if the number is divisible by 3.

# Input 1:
# A = [1, 2, 3]
# Input 2:
# A = [1, 0, 0, 1, 2]

# Output 1:1
# Output 2: 0
def divisible(a):
    b=sum(a)
    if b%3==0:
        return 1
    else:
        return 0
a=list(map(int,input().split()))
print(divisible(a))