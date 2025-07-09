from collections import deque
class RecentCounter:

    def __init__(self):
        self.array = deque()
        

    def ping(self, t: int) -> int:
        self.array.append(t)
        
        while self.array and self.array[0] < t - 3000:
            self.array.popleft()

        return len(self.array)
        


# original (very very BAD and slow):
# class RecentCounter:

#     def __init__(self):
#         self.array = [[]]
        

#     def ping(self, t: int) -> int:
#         if t >= (t - 3000):
#             self.array.append(t)
            
#         result = []
#         for x in self.array:
#             if x and x >= (t - 3000):
#                 result.append(x)
#         return len(result)
