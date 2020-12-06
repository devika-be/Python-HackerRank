# Problem link : https://www.hackerrank.com/challenges/py-if-else/problem

#ANS-

#!/bin/python3 

N = int(input())
if N % 2 != 0:
    print("Weird")

else:
    if N >= 6 and N <= 20:
        print("Weird")

    else:
        print("Not Weird")
