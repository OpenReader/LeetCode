# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        # get the length of list
        L = 0
        cur = head
        while cur != None:
            cur = cur.next
            L += 1
        if L == 1:
            return True
        
        # reverse half of list
        cur, pre = head, None
        i = 0
        while i < L//2:
            i += 1
            cur.next, cur, pre = pre, cur.next, cur
        
        print(cur.val, pre.val)
        if L % 2 != 0:
            cur = cur.next
            
        # compare two part
        while cur != None:
            if cur.val != pre.val:
                return False
            cur, pre = cur.next, pre.next
        
        return True