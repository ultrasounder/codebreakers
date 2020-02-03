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


        anagrams = {} # create a hashtable of anagrams
        for word in str: #Iterate through the entire string
            sortedWord = "".join(sorted(word)) # create a new string by sorting the words in the string 
            if sortedWord in anagrams:# Check if the sorted word is present in the hashmap O(1)
                anagrams[sortedWord].append(word) # if its great, then add it to the hasmap
            else:
                anagrams[sortedWord] = [word]# if not 
        return list(anagrams.values())



