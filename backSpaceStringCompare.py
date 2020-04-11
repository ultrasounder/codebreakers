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

        for char in S: # we want to be looping through string T, not S
            if char != '#':
                t.append(char)
            elif t:
                t.pop()
                
        while s:
            current = s.pop()
            if not t  or t.pop() != current:
                return False
        return not s  and not t 

'''
Your solution looks good! The stack approach is spot on. We are always looking back at the most recent element,
so the stack is the right approach. I just left one inline comment. Otherwise, this is a great linear solution!
'''
