def reverseList(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # create null node as the end of the reversed list
        #     n  h 
        #   null 1 -> 2 -> 3 -> 4
        node = None
        
        while head:
            # place next node list in temp
            temp = head.next
            
            head.next = node    # now the node after head is the one behind
            node = head     # now the node becomes the current head
            head = temp     # now the new head is the node list in temp

        return node