def process_sequence(x, y):
    answer = ''
    count = 0
    index = 0

    for i in range(x):
        answer += '+'
        if (y[i] % 2) == 1:
            count += 1
            index = i

    if (count % 2) == 0 and index == 0:
        answer = answer[:index] + 'x' + answer[index + 1:]

    if (count % 2) == 0 and index != 0:
        answer = answer[:index - 1] + 'x' + answer[index:]

    answer = answer[:-1]

    return answer

x = int(input())
y = list(map(int, input().split()))

print(process_sequence(x, y))

