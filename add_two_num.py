
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None
def to_num(node):
    num = 0
    m = 1
    while True:
        num += m * node.val
        node = node.next
        m *= 10 
        if not node:
            break
    return num
def to_list_node(num):
    root = None
    cur = None
    while True:
        val = num % 10 
        num = num / 10
        newNode = ListNode(val)
        if not root:
            root = newNode
        else:
            cur.next = newNode
        cur = newNode
        if num < 1:
            break
    return root
class Solution(object):
 
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return to_list_node(to_num(l1) + to_num(l2))