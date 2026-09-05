class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        values = arr[0::2] + arr[1::2]

        curr = head
        for value in values:
            curr.val = value
            curr = curr.next

        return head