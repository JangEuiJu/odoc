# 실행 단축키 shift + f11

import sys
input = sys.stdin.readline

def mat_mult(a, b, MOD):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]
    ]

def mat_pow(mat, n, MOD):
    if n == 1:
        return mat
    if n % 2 == 0:
        half = mat_pow(mat, n // 2, MOD)
        return mat_mult(half, half, MOD)
    else:
        return mat_mult(mat, mat_pow(mat, n - 1, MOD), MOD)

def fib(n):
    MOD = 1_000_000_007
    if n == 0:
        return 0
    mat = [[1, 1], [1, 0]]
    result = mat_pow(mat, n, MOD)
    return result[0][1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()