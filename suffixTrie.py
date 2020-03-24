class suffixTrie:
    def __init_(self, string):
        self.root = {}
        self.endSymbol = '*'
        self.populateSuffixTreeFrom(string)

    def populateSuffixTreeFrom(self, string):

        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
        

