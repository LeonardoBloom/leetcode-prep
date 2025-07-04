nums = [1,2,3]
n = len(nums)
res, sol = [], []

def backtrack(i):

    if i == n:
        res.append(sol[:])
        return

    # dont pick nums at [i]: go LEFT
    backtrack(i + 1)

    # pick nums at i: go RIGHT
    sol.append(nums[i])
    backtrack(i+1) 
    sol.pop()

backtrack(0)
print(res)


