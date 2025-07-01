from collections import defaultdict

def uniqueOccurrences(arr):
        
        # dictionary to store occurence of each value
        counts = defaultdict(int)

        for number in arr:
            counts[number] += 1

        occur = list(counts.values())
        countSet = set(occur)

        return len(occur) == len(countSet)