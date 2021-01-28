#Problem Link : https://www.hackerrank.com/challenges/python-lists/problem

#Ans :

if __name__ == '__main__':
    N = int(input())
    listt=[]
    while N>0:
        x= list(map(str,input().split()))
        if x[0] == "print":
            print(listt)
        elif x[0] == "insert":
            listt.insert(int(x[1]),int(x[2]))
        elif x[0] == "remove":
            listt.remove(int(x[1]))  
        elif x[0] == "append":
            listt.append(int(x[1]))  
        elif x[0] == "sort":
            listt.sort()
        elif x[0] == "pop":
            listt.pop()
        elif x[0] =="reverse":
            listt.reverse()
        N -= 1
