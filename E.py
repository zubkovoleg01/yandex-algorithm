def startup_profit(n, k, d):
    n_str = str(n)
    remainder = n % k

    if remainder == 0:
        return n

    for i in range(1, d + 1):
        for digit in range(1, 10):
            new_profit = int(n_str + str(digit) * i)
            if new_profit % k == 0:
                return new_profit
        return -1

# Считываем данные
n, k, d = map(int, input().split())

# Выводим результат
print(startup_profit(n, k, d))

