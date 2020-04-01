# jump game
# house robber
# coming up with recurrence relations


# to solve dp problems:
# 1. think 10 steps into the problem, assume we have the optimal solution to everything before hand/ think of setp right before solution -> recurrence relation
# 2. think of how to build this up from the bottom
# 3. think of base case

def houseRobber(arr):
    # at the end of our array, we can either choose the current index we are on and the entry from 3 houses back or 2 houses back
    # arr = [1,7,9] -> amount of money stashed at each house

    # recurrence -> we can rob a house 2 houses previous or 3 houses previous
    # this builds up from the bottom -> check'
    #  given dp index i will represent the best we can do if we rob arr[i]
    # base cases-> dp[0] = arr[0], dp[1] = arr[1], dp[2] = arr[0] + arr[2]
    # dp[i] = max(dp[i-2], dp[i-3]) + arr[i]
    n = len(arr)
    dp = [0] * n
    # dp[0], dp[1], dp[2] = arr[0], arr[1], arr[0] + arr[2] # base cases
    # for i in range(3, n):
    #     dp[i] = max(dp[i-2], dp[i-3]) + arr[i] # recurrence
    # print(dp)
    # return max(dp[-1], dp[-2])
    dp[0] = 0
    dp[1] = arr[0]
    for i in range(1, n):
        val = arr[i]
        dp[i+1] = max(dp[i], dp[i-1] +  val)
    return dp[n]



# print(houseRobber([2,7,9,3,1]))


def jumpGame(arr):
    # bottom up to start!
           # 0 1 2 3 4
    # arr = [2,3,1,1,4]
    # dp =  [O O O O O
    # for a given i, we can jump from i through arr[i] + i
    n = len(arr)
    dp = [False] * n
    dp[0] = True
    
    for i in range(n):
        if dp[i] == True: # we can rach this point, let's expand
            if i + arr[i] + 1 == n:
                return True
            for j in range(arr[i]):
                dp[i+j+1] = True
    return False
print(jumpGame([2,3,1,1,4]))
print(jumpGame([3,2,1,0,4]))
    
# bottom up
# def fib(n):
#     if n < 2:
#         return 1
#     x = y = z = 1
#     for i in range(n - 2):
#         z = x + y
#         x = y
#         y = z
#     return z
#     # 1 1 2 3 5 8...
    # recurrence n-1 + n-2
    # dp = [1] * n # base case
    # for i in range(2, len(n)):
    #     dp[i] = dp[i-1] + dp[i-2] # recurrence
    # return dp[-1]
# dp = {} # memoization
# def topDown(n):
#     if n < 3: # base case
#         return 1
#     if n in dp: # if we have seen that n before, give us the answer that we remembered!
#         return dp[n]
#     dp[n] = topDown(n-1) + topDown(n-2) # if we have calculated an n before, remember it
#     return dp[n]


             #        10
             #    9        8
             # 8     7


# print(fib(3))
# print(topDown(50))