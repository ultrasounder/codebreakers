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
