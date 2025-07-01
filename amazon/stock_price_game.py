

stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
queries = [6, 5, 4]

def predictAnswer(stockData, queries):

    l = 0;
    r = 0;
    result = []

    for x in queries:
      stockValue = stockData[x - 1]
      while l != 0 or r != len(stockData):
        for a in range(x -2, 0, -1):
          if stockData[a] < stockValue:
            l = a
            break
        for a in range(x, len(stockData)):
          if stockData[a] < stockValue:
            r = a
            break
        if abs(l - x)-1  <= abs(r - x-1):
            result.append(l+1)
            break
        else:
            result.append(r+1)
            break

    return result


print(predictAnswer(stockData, queries))