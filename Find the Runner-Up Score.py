#Problem Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

#Ans : 

import heapq

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    a = heapq.nlargest(2, arr)
    print(a[1])
