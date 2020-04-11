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
    
'''
Nice job using the set to see if we are in a cycle. This makes sure we do not get caught in an infinite loop. However, for a 
different reason, we still get caught in an infinite loop. Notice that current is going to be made into a float thus making sum
into a float and getting smaller and smaller, but never repeating (we get asymptotically close to 0). This gets us stuck in an infinite
loop. We also want to be squaring the number which if we want to take 9 to the power of 2, we can write 9**2. Also, we really only need
to loop through our numbers once, so we can just use a for loop inside the while loop and sum all these numbers, then do something
with the sum. The code for this flow would like this:

class Solution:
    def isHappy(self, n):
        seen = set()
        fast = [i**2 for i in range(10)]
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            curSum = 0
            for num in str(n):
                curSum += fast[int(num)]
            n = curSum
        return False
        
You will also notice I added the squared numbers (0-9) to a list so we do not repeat this computation a bunch of times and we
can just use this as a dp/lookup table of sorts. This approach is similiar to what you were doing, but uses the for loop
to capture the behaviour. Using the for loop also reduces our chances of writing indexing bugs or even an infinite loop.
Let me know if any of this does not make sense and we can talk about it. Hope this helps!
'''
