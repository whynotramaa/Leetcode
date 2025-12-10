class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        ptr1 = head
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

    def lengthLoop(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: #LOOP EXISTS
                count = 1
                fast = fast.next

                while fast != slow:
                    count+=1
                    fast = fast.next
                return count

        return 0
