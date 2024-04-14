def stadium(length, position1, velocity1, position2, velocity2):
    t_values = []
    center = (position1 + position2) / 2 % (length / 2)
    avg_velocity = (velocity1 + velocity2) / 2

    position1 = position1 % length
    position2 = position2 % length

    if avg_velocity > 0:
        center = length / 2 - center

    if not center:
        t_values.append(center)

    if avg_velocity:
        t_values.append(center / abs(avg_velocity))

    delta_position = position2 - position1

    if not delta_position:
        t_values.append(delta_position)

    delta_velocity = velocity2 - velocity1

    if delta_position * delta_velocity > 0:
        delta_position = length - abs(delta_position)

    if delta_velocity:
        t_values.append(abs(delta_position) / abs(delta_velocity))

    if t_values:
        return min(t_values)


length, position1, velocity1, position2, velocity2 = map(int, input().split())
res = stadium(length, position1, velocity1, position2, velocity2)
if res is None:
    print('NO')
else:
    print('YES')
    print('{:.10f}'.format(res))

