class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sortedWords = ["".join(sorted(w)) for w in str] # rearrange each letters in each words

        # indices = [i for i in range(len(str))]

        # indices.sort(key = lambda x: sortedWords[x])

        # result = []

        # currentAnagramGroup = []
        # currentAnagram = sortedWords[indices[0]]

        # for index in indices:
        #     words = str[index]
        #     sortedWord = sortedWords[index]

        #     if sortedWord == currentAnagram:
        #         currentAnagramGroup.append(str)
        #         continue
        #     result.append(currentAnagramGroup)
        #     currentAnagramGroup = [str]
        #     currentAnagram = sortedWord

        # result.append(currentAnagramGroup)

        # return result
        '''
        Overall the solution looks great! The code quality is very high. If the longest string is K and we have
        N words, then our runtime will be O(N*K*log(K)). This is pretty good! We can improve the log by using the algorithm we
        discussed on Sunday: count letters of a given word in a string, record this as a tuple, hash the tuple to a list of those
        words. We then are linear in both N and K, giving us O(N*K). Nice work!
        '''

        anagrams = {} # create a hashtable of anagrams
        for word in str: #Iterate through the entire string #Variable is named strs, not str. Very minor detail
            sortedWord = "".join(sorted(word)) # create a new string by sorting the words in the string 
            if sortedWord in anagrams:# Check if the sorted word is present in the hashmap O(1)
                anagrams[sortedWord].append(word) # if its great, then add it to the hasmap
            else:
                anagrams[sortedWord] = [word]# if not 
        return list(anagrams.values())



