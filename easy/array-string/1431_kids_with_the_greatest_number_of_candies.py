def kidsWithCandies(candies, extraCandies):

    # ORIGINAL
    # max = 0
    # result = []
    # for candy in candies:     ## apparently can be replaced by max(candies)
    #     if candy > max:
    #         max = candy

    # for candy in candies:
    #     if candy + extraCandies >= max:
    #         result.append(True)
    #     else:
    #         result.append(False)

    # OPTIMIZED
    result = []

    for candy in candies:
        if max(candies) <= candy + extraCandies:
            result.append(True)
        else:
            result.append(False)

    return result


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
