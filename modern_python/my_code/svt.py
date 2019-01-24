def svt(distance = None, speed = None, time = None):
    if distance is None:
        return f'Distance = {speed * time}'
    elif speed is None:
        return f'speed = {distance / time}'
    else:
        return f'time = {distance / speed}'

print(svt(speed=10, time=4))
print(svt(distance=10, time=4))
print(svt(speed=10, distance=40))
