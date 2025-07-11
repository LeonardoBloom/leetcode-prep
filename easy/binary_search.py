def guess(n):
    pick = 6
    if n > pick:
        return -1
    elif n < pick:
        return 1
    else:
        return 0

def binary(start, end):
            
    mid = (start + end) // 2
    guessed = guess(mid)

    if guessed == -1:
        return binary(start, mid + 1)
    elif guessed == 1:
        return binary(mid - 1, end)
    elif guessed == 0:
        return mid

print(binary(1, 10))

# left, right = 1, n

# while left <= right:
#     mid = (left + right) // 2
#     guessed = guess(mid)

#     if guessed == 0:
#         return mid
#     elif guessed == -1:
#         right = mid - 1
#     else:
#         left = mid + 1