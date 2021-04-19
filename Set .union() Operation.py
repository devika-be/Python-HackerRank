#Problem Link : https://www.hackerrank.com/challenges/py-set-union/problem

#Ans :

input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
print(len(a.union(b)))
