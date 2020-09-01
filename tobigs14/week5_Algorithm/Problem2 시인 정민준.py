T = int(input())
colors = [list(map(int, input().split())) for _ in range(T)]


check = [colors[0]]
def solve(colors, n) :
    red = colors[n][0] + min(check[n-1][1], check[n-1][2])
    green = colors[n][1] + min(check[n-1][0], check[n-1][2])
    blue = colors[n][2] + min(check[n-1][0], check[n-1][1])
    return [red, green, blue]


for i in range(1, T) :
    check.append(solve(colors, i))


print(min(check[-1]))