class Listnode:
    def __int__(self,val = 0):
        self.val
        self.next = next

class Solution:
    def CycleLinkedList(self,head: Listnode)->Listnode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            else:
                return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

