#coding utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists( l1: ListNode, l2: ListNode) -> ListNode:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val  < l2.val:
        L=ListNode(l1.val)
        L.next = mergeTwoLists(l1.next,l2)
        return L
    else:
        L = ListNode(l2.val)
        L.next = mergeTwoLists(l1, l2.next)
        return L


def init_listNode(l)-> ListNode:
    if l:
        li=ListNode(l[0])
        li_head= li
    else:
        return ListNode(None)
    for i in l[1:]:
        li_new=ListNode(i)
        li.next=li_new
        li = li_new
    return li_head
def print_listNode(l: ListNode):
    if  ( l == None):
        print('None')
        return
    while ( l .next):
        print(l.val,end='->')
        l = l.next
    else:
        print(l.val)
def main():
    l1,l2=[1,2,4], [1,3,4]
    L1 = init_listNode(l1)
    L2 = init_listNode(l2)
    print_listNode(L1)
    print_listNode(L2)
    L = mergeTwoLists(L1, L2)
    print_listNode(L)

if __name__ == '__main__':
    main()