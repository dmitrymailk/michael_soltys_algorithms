def rem(x, y):
    q = 0
    r = x
    while y <= r:
        r = r - y
        q += 1
    return q, r


def gcd(m, n):
    p, r = rem(m, n)
    init_m = m
    init_n = n

    parts = [p]
    steps = 1

    while r > 0:
        m = n
        n = r
        p, r = rem(m, n)
        parts.append(p)
        steps += 1

    a = 0
    b = 1
    for i in range(steps-1, -1, -1):
        _a = a
        a = b - parts[i] * a
        b = _a

    print(b*init_m + a*init_n, n)
    return n


print(gcd(546, 212))
