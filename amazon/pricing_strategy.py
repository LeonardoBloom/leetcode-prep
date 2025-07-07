n = 5
# price = [3,3,2,3,2,3]
# price = [3, 2, 3, 1]
price = [1, 2, 3, 4, 5]

def findPrice(price):
    
    subarrays = []

    for length in range(len(price)):
        p = 0
        res = []
        while p < len(price):
            offset = p + length + 1
            res.append(price[p:offset])
            # print(res)
            p += 1
            if offset == len(price):
                break
        subarrays.append(res)
    for x in subarrays:
        print(x)
    result = []

    for array in range(len(subarrays)):
        finalSet = set(subarrays[array][0])
        for number in range(1, len(subarrays[array])):
            finalSet &= set(subarrays[array][number])
        print("finalSet: ", list(finalSet))
        if finalSet:
            result.append(min(finalSet))
        else:
            result.append(-1)

    print(result)

findPrice(price)