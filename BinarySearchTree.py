def inOrder(node, orderedNodes):
    if (node!=None):
        inOrder(node.left, orderedNodes)
        orderedNodes.append(node.data)
        inOrder(node.right, orderedNodes)
        
def check_binary_search_tree_(root):
    ordered = []
    inOrder(root, ordered)
    for i in range(len(ordered)-1):
        if (ordered[i]>=ordered[i+1]):
            return False
    return True