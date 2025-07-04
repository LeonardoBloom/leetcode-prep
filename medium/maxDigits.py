def getMaxLuckyNumber(x, y, n):
    max_number = ''

    # Try all possible counts of digit x
    for count_x in range(n // x + 1):
        rem = n - count_x * x
        if rem % y != 0:
            continue
        count_y = rem // y
        
        digits = [x] * count_x + [y] * count_y
        digits.sort(reverse=True)  # to form the biggest number
        lucky_number = ''.join(map(str, digits))
        
        if lucky_number > max_number:
            max_number = lucky_number

    return int(max_number)

print(getMaxLuckyNumber(3,4,13))