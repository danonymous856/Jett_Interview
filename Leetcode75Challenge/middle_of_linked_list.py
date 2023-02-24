class Listnode:
    def __int__(self, val = 0):
        self.val =val
        self.next = next

class Solution(Listnode):
    def middleNode(self,head:Listnode)->Listnode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

a = Solution()
a.middleNode([1,2,3,4,5])