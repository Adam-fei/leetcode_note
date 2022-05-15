from typing import ListNode


# 3sum 外面包了一层循环
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


if __name__ == "__main__":
    solution = Solution()

    head = [1,2,3,4,5]

    print(solution.reverseList(head))
