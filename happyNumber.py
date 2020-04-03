class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()#hashset to store all the numbers seen

        while n is not 1:
            current = n
            sum = 0
            while current is not 0:
                sum += (current % 10) * (current % 10)
                current /= 10
            if sum in seen:
                return false
            seen.add(sum)
            n = sum
        return True