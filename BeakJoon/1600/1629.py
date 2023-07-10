import sys

A, B, C = map(int, sys.stdin.readline().split())


def power(A, B, C):
    if B == 1:
        return A % C
    else:
        temp = power(A, B // 2, C)
        if B % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * A % C


print(power(A, B, C))
