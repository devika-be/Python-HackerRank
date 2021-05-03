#Problem Link : https://www.hackerrank.com/challenges/py-the-captains-room/problem

#Ans :

k,arr = int(input()),list(map(int,input().split()))
s = set(arr)
print(((sum(s)*k)-(sum(arr)))//(k-1))
