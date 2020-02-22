class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirstSearch(self, array):
        Queue = [self] # initalizing the Queue with the root node
        while len(Queue) > 0:
            current = Queue.pop(0)
            array.append(current.name)
            for child in current.children:
                Queue.append(child)
        return array

        

