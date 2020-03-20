import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:


        if not words:
            return False

        sorted(words, key=len)
        dp = collections.defaultdict(int)
        # words.sort(key=len)
        result = 0
        for word in words:
            for index in range(len(word)):
                char_excluded_string = word[:index] + word[index+1:]
                if char_excluded_string in dp:
                    dp[word] = max(dp[char_excluded_string] + 1, dp[word])
                else:
                    dp[word] = max(dp[word], 1)
            result = max(dp[word], result)
        return result
    
    '''
    Nice work. I have to give it to you: that was one weird bug! So it looks like what you are doing with the sorted function
    is not actually sorting the list by length. Try using the line that I commented out and see how the program runs. The prorgram
    is doing exactly what it should, it is just the words were not properly sorted. Your solution was much closer than you thought!
    Awesome job!
    '''


    #     StringChains = {} #Hash map to store all the strings
    #     for string in words:
    #         StringChains[string] = {"nextString": "", "maxChainLength": 1}

    #     sortedStrings = sorted(strings, key=len) #sorting the strings
    #     for string in sortedStrings:
    #         findLongestStringChain(string, stringChains)
    #     pass

    # def findLongestStringChain(string, stringChains):
    #     for i in range(len(string)):
    #         smallerString = getSmallerString(string, index)
    #     if smallerString not in StringChains:
    #         continue
    #     tryUpdateLongestStringChain(string, smallerString, stringChains)



    # def getSmallerString(string, index):
    #     return string[0:index] + string[index + 1 :]

    # def tryUpdateLongestStringChain(currentString, smallerString, stringChains):
    #     smallerStringChainLength = stringChains[smallerString]["maxChainLength"]

       


