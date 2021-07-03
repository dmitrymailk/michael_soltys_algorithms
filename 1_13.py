def strange_algo(x, y):
    z = 0
    step = 0
    while x != 0:
        step += 1
        some = (x % 2)*" not"
        print(f"x={x} y{some}={y} z={z}")
        if x % 2 == 1:
            z = z + y

        x = x // 2
        y = y * 2
    some = (x % 2)*" not"
    print(f"x={x} y{some}={y} z={z}")

    print(f"Z={z}")
    print(f"steps = {step}")


def strange_algo_2(x, y):
    power = 1
    z = 0
    while x // power > 0:
        if x % power == 1:
            print(z)
            z += y * power
        power *= 2
    print(f"Z={z}")


strange_algo_2(17, 3)
