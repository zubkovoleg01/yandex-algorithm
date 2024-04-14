def calculate_rounds(x, y, p):
    remaining_soldiers = 0
    rounds = 0

    if x > p:
        extra_soldiers = x - p
        return (y + extra_soldiers - 1 - x) // extra_soldiers + 1

    while x < y and x > 0:
        rounds += 1
        y -= x
        x -= remaining_soldiers
        remaining_soldiers += p

    if y > 0:
        rounds += 1
        extra_soldiers = x - y
        remaining_soldiers -= extra_soldiers
        x -= remaining_soldiers

    while x > 0 and remaining_soldiers > 0:
        rounds += 1
        remaining_soldiers -= x
        x -= remaining_soldiers

    if remaining_soldiers <= 0:
        return rounds
    else:
        return -1

x = int(input())
y = int(input())
p = int(input())

print(calculate_rounds(x, y, p))