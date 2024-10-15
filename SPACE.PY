'''
 Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
'''
set={5,3,1,4,5,2}
a=int(input("enter number of values:"))
for i in range(a):
    n=int(input())
print(*set)   
