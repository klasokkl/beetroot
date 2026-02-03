def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("step не может быть равен 0")

    current = start

    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step
