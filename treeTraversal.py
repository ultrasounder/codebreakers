#iterative inorder 

def inOrderTraversal(root):
    stack = [] #keep track of previously seen nodes
    node = root#make the current node the root. Start from the node, left child, current node and right chilld
    while(node): # do pre-processing to traverse dowm th left side and record previously seen nodes
        stack.append(node)
        node = node.left# pivot towards the left sub-tree to traverse down the entire sub-tree

        while(stack): #while there are nodes that we have seen and not processed
            cur = stack.pop()
            print(cur.val) #if there are no more left children then we can print it
            if cur.right: # now we have to add its right child to seen and go down its left subtree
                node = curr.right
                while(node): # go down left subtree
                    stack.append(node)
                    node = node.left

#recursive postorder: left, curre,t right

def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.val)

#recursive in order:left, current, right
def inorderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    printl(root.val)
    inorderTraversal(root.right)

#recursive pre-order- current, left and right
def PreOrderTraversal(root):
    if root is None:
        return
    print(root.val)
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)

#iterative level order

def level_order_traversal(root):
    queue = Queue()
    queue.enqueue(root)
    while len(queue) > 0:
        x = queue.dequeue()
        if x is not None:
            print(x.val)
            queue.enqueue(x.left)
            queue.enqueue(x.right)
            

