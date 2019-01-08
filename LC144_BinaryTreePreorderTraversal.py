#coding utf-8
#144. Binary Tree Preorder Traversal
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def make_a_Binary_Tree_by(li):
    if li[0]!=None:
        node = TreeNode(li.pop(0))
        node.left=make_a_Binary_Tree_by(li)
        node.right=make_a_Binary_Tree_by(li)
    else:
        return li.pop(0)
    return node
def preorder_traversal(root):
    li=[]
    if root!=None:
        li+=[root.val]
        li+=preorder_traversal(root.left)
        li+=preorder_traversal(root.right)
    else:
        return []
    return li
def main():
    l = [10, 7, 4,None,None, 9,None,None, 13, None, 15,None,None]
    root=make_a_Binary_Tree_by(l)
    print('\t\t',root.val)
    print('\t',root.left.val,'\t\t  ',root.right.val)
    print(' ',root.left.left.val,'   ',root.left.right.val,' ',root.right.left,'  ',root.right.right.val)
    print(preorder_traversal(root))
if __name__ == '__main__':
    main()