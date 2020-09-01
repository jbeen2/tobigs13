M, N = map(int, input().split())

prev = [1] * (M+1)
next = [1] + [0] * M

def solve(M,N,prev) :
    for _ in range(N-1) :
        for m in range(1,M+1) :
            next[m] = next[m-1] + prev[m]

        prev = next.copy()

    return prev[-1] % 10000

print(solve(M,N,prev))


# d = [[1]+[0]*(M)]*(N+1)
# d[1] = [1]*(M+1)
#
# def solve(m,n) :
#     if d[n][m] > 0:
#         return d[n][m]
#
#     d[n][m] = solve(m-1, n) + solve(m, n-1)
#     return d[n][m]
#
# def bottom_up(m,n) :
#     for i in range(2, n):
#         for j in range(i+1, m):
#             d[i][j] = d[i-1][j] + d[i][j-1]
#
#     return d[n][m]


# for i in range(2, N+1): -> j가 n에 영향받아서 안된다
#     for j in range(i + 1, M+1):
#         d[i][j] = d[i - 1][j] + d[i][j - 1]

#print(bottom_up(M,N))

