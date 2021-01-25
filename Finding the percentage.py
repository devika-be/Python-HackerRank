#Problem Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem

#Ans :

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    summ = sum(student_marks[query_name])
    print("%.2f" % (summ/3))
