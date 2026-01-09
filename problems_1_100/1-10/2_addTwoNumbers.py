# Definition for singly-linked list.
from typing import Optional

#Works on PyCharm but not on leetcode,
# judging from discussion it is because I am expected to add them together as I come across them
# and not by making them their own ints first then adding them together (which is my current code)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cursor = l1
        i = 1
        while cursor:
            n = cursor.val
            n = n * i
            num1 += n
            cursor = cursor.next
            i *= 10
        # print(num1)
        cursor = l2
        i = 1
        while cursor:
            n = cursor.val
            n = n * i
            num2 += n
            cursor = cursor.next
            i *= 10
        # print(num1 + num2)

        num3 = num1 + num2
        rn = num3 % 10
        num3 = (num3 - rn) / 10
        head = ListNode(rn)
        # node.val = rn

        current = head
        while num3 > 0:
            # print("hi")
            rn = num3 % 10
            new_node = ListNode(int(rn))
            current.next = new_node
            current = new_node
            num3 = (num3 - rn) / 10
            # prev = new_node

        # print(head.next)
        return head

def create_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def main():
    solution = Solution()
    l1 = create_linked_list([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    l2 = create_linked_list([5,6,4])
    # l1 = create_linked_list([9,9,9,9,9,9,9])
    # l2 = create_linked_list([9,9,9,9])
    cursor = solution.addTwoNumbers(l1, l2)
    while cursor:
        print(cursor.val, end=",")
        cursor = cursor.next

if __name__ == '__main__':
    main()