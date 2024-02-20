# https://leetcode.cn/problems/add-two-numbers/

# 参考：https://cloud.tencent.com/developer/article/1818199

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = node = ListNode(0)
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum_ = a + b + carry
            carry = sum_ // 10
            val = sum_ % 10
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry != 0:
            node.next = ListNode(carry)
        return dummy.next
    
    def subTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        两个数都是非负整数
        逻辑：先比较2个数数的大小，转化为大数见小数计算
        """
        def compare(l1, l2):
            # 判断两个数的大小
            ri = 1 # 1表示l1>=l2, -1表示l1<l2
            while l1 and l2:
                if l1.val < l2.val:
                    ri = -1
                l1 = l1.next
                l2 = l2.next
            if l2: ri = -1 # l2的位数更多
            if l1: ri = 1
            return ri
                

        carry = 0
        dummy = node = ListNode(0)

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            # if 
