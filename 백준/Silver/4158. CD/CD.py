import sys

while True:
    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0:
        break

    cd_list_A = [int(sys.stdin.readline()) for _ in range(N)]
    cd_list_B = [int(sys.stdin.readline()) for _ in range(M)]

    index_A, index_B = 0, 0
    count = 0

    while index_A < len(cd_list_A):
        if cd_list_A[index_A] == cd_list_B[index_B]:
            index_A += 1
            index_B += 1
            count += 1
        elif cd_list_A[index_A] < cd_list_B[index_B]:
            index_A += 1
        elif cd_list_B[index_B] < cd_list_A[index_A]:
            index_B += 1

    print(count)