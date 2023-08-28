import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
gems = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()
result = 0
tmp = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)
