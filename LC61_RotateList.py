#coding utf-8
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#思路1：
#先将原序列连成环，再找到输出的头结点，最后在头节点前将环打断，输出头
#执行用时 :56 ms, 在所有Python3提交中击败了91.41%的用户
# 内存消耗 :13.1 MB, 在所有Python3提交中击败了80.00%的用户
def rotateRight( head: ListNode, k: int) -> ListNode:
    if not head:
        return None
    node = head
    l = 1
    while node.next:
        node = node.next
        l += 1
    else:
        node.next = head
    t = l - (k % l)
    while t >1:
        head = head.next
        t -= 1
    R = head.next
    head.next =None
    return R

#思路2：
#找到输出的头位置，将原序列打断，最后接上原头结点和尾节点
#执行用时 :60 ms, 在所有Python3提交中击败了81.68%的用户
#内存消耗 :13 MB, 在所有Python3提交中击败了91.20%的用户
def rotateRight1( head: ListNode, k: int) -> ListNode:
    if not head:
        return None
    node = head
    l = 1
    while node.next:
        node = node.next
        l += 1
    else:
        node.next = head
    k = k%l
    node = head
    while k < l-1:
        node = node.next
        k +=1
    else:
        R = node.next
        node.next = None
    return R


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
    l = [1,2,3,4,5]
    l = [0,1,2,3]
    #l = []
    k = 2
    L = init_listNode(l)
    print_listNode(L)
    R = rotateRight1(L , k)
    print_listNode(R)

if __name__ == '__main__':
    main()