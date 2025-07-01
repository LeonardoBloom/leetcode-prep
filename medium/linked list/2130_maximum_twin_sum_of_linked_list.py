def pairSum(head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if head == None: return None
        fast = head
        slow = head
        left = []
        right = []

        maxSum = 0

        while fast != None and fast.next != None:
            left.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        print(left)

        i = len(left) - 1
        
        while i >= 0:
            twinSum = slow.val + left[i]
            slow = slow.next
            print(twinSum)
            if twinSum > maxSum:
                maxSum = twinSum
            i -= 1

        return maxSum