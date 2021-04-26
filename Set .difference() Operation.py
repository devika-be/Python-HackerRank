#Problem Link : https://www.hackerrank.com/challenges/py-set-difference-operation/problem

#Ans :

input()
english = set(map(int,input().split()))
input()
french = set(map(int,input().split()))
print(len(english.difference(french)))
