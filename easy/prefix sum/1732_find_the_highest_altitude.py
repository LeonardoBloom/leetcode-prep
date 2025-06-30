def largestAltitude(gain):
    alts = [0]

    for i in range(len(gain)):
        alts.append(alts[i] + gain[i])

    return max(alts)