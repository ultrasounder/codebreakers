class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set() #initalize a hashset
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
        for i in seen:
            return i
'''
Looks great! This is a great solution and probably the one you would think of in an interview.
We can also do this in one line: return 2 * sum(set(nums)) - sum(nums)
The idea here we get the expected sum (on the left) minus the actual (on the right) will give us the number that is not counted twice.
Same space and time, but more concise and mathy :)
Looks great!
'''
