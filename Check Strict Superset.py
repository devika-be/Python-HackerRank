#Problem Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem

#Ans :

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
