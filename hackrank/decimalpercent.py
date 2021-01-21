from decimal import *
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    decilist = [Decimal("%.2f" % e) for e in list(query_scores)]

    sum = 0
    for i in decilist:
        sum += i
    result = sum / len(decilist)
    print(result)