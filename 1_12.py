def is_power_2(n):
    while n > 1:
        if n % 2 != 0:
            return "no"
        n = n / 2

    return 'yes'


for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16]:
    print(f"{item} - {is_power_2(item)}")
