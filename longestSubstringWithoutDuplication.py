<<<<<<< HEAD
=======
# Time O(n), Space O(min(n, a))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_seen = {}#hold indices of the most recent appearances of ths characters in the string
        longest = [0, 1] #stating and ending index of the current longest substring
        startIndex = 0 #Intialize the startIndex pointer
        for i, char in enumerate(s): # iterate through the string and obtain indices
            if char in last_seen: # If the char at index i is already in the hashmap
                startIndex = max(startIndex, last_seen[char] + 1) # update the start index by looking at ther max of startindex and the hashmap
            if longest[1] - longest[0] < i + 1 - startIndex: # if the difference beween the end of the longest substring start and end
                longest = [startIndex, i + 1] # we update the start index 
            last_seen[char] = i# update the last seen character to the hashtable
        return s[longest[0]:longest[1]] # return the slice the longest substring
    
    '''
    Awesome solution with 0 syntax errors. Nice work! You make a cool modification to this by actually jumping the pointer
    ahead to the next character. This interestingly doesn't improve the run time because the longest substring we can have is 26
    letters, which is a constant. We could also save a bit of memory by using a set instead of a dictionary where we loop over 
    every character. This would not change our big O run time or memory complexity, it is a just a different way of doing the problem
    in case the interviewer asks you to expand on the solution. Nice work!
    '''
>>>>>>> 9d00c49b7c8f3ddb432c07836cf10fc54f4635af
