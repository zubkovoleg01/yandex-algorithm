def trees(P, V, Q, M):
    result = 0

    a = P - V, P + V
    b = Q - M, Q + M

    if a[0] <= b[0] and a[1] >= b[1]:
        result = a[1] - b[0] + 1
    elif a[1] < b[0]:
        result = a[1] - a[0] + b[1] - b[0] + 2
    elif a[1] >= b[0]:
        result = b[1] - a[0] + 1

    return result

P, V = map(int, input().split())
Q, M = map(int, input().split())

print(trees(P, V, Q, M))