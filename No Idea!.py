#Problem link : https://www.hackerrank.com/challenges/no-idea/problem

#Ans :

input()
m = list(input().split())
a = set(input().split())
b = set(input().split())
print(sum((i in a) - (i in b) for i in m))
