class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for number in num:
            while(stack and k and int(stack[-1]) > int(number)):
                stack.pop()
                k -= 1
            stack.append(number)
        if k:
            stack = stack[:-k]


        curr = 0
        while() curr < 