    class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:


        '''Remember the last state, remember things that we have seen in a particualr order. Stack''''
        s = [] # hold character s
        t = []

        for char in S:
            if char != '#':
                s.append(char)
            elif s:
                s.pop()

        for char in S:
            if char != '#':
                t.append(char)
            elif t:
                t.pop()
                
        while s:
            current = s.pop()
            if not t  or t.pop() != current:
                return False
        return not s  and not t 


            

