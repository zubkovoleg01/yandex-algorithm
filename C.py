def min_key_presses(n, spaces_needed):
    total_presses = 0
    for spaces in spaces_needed:
        total_presses += spaces // 4
        remainder = spaces % 4
        total_presses += (remainder // 3) * 2
        total_presses += remainder % 3
    return total_presses

n = int(input())
spaces_needed = [int(input()) for _ in range(n)]

print(min_key_presses(n, spaces_needed))
