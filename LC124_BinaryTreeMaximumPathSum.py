# -*- coding: utf-8 -*-
#

class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def creatTreeNodeBy(l):
    root = TreeNode(l.pop(0))
    node = root
    lay = []
    while l:
        t = l.pop(0)
        if t :
            node.right = TreeNode(t)
            lay.append(node.right)
        t = l.pop(0)
        if t:
            node.left = TreeNode(t)
            lay.append(node.left)
        node = node.right
    else:
        return root
def maxPathSum(root: TreeNode) -> int:
    return
def main():
    l = [-10,9,20,None,None,15,7]

    maxPathSum()

if __name__ == '__main__':
    main()