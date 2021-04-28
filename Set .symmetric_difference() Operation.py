#Problem link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

#Ans :

input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
print(len(a.symmetric_difference(b)))
