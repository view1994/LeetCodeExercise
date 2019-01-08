#coding utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    li=None
    if l1:
        li=ListNode(l1.val)
        l1_next=l1.next
    else:
        l1_next=None
        if not l2:
            return None
    if l2:
        li_new=ListNode(l2.val)
        if li:
            li.next=li_new
        else:
            li=li_new
        if l2.next:
            l2_next=l2.next
        else:
            l2_next=None
        li_new.next=mergeTwoLists(l1_next,l2_next)
    return li

def init_listNode(l):
    if l:
        li=ListNode(l[0])
    else:
        return None
    for i in l[1:]:
        li_new=ListNode(i)
        li.next=li_new
    return li
def main():
    l1,l2=[], [0]
    print(mergeTwoLists(init_listNode(l1), init_listNode(l2)))

if __name__ == '__main__':
    main()