class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nigga = epstein = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                epstein.next = list1
                list1 = list1.next 
            else: 
                epstein.next=list2
                list2 = list2.next
            epstein=epstein.next
        epstein.next= list1 or list2
        return nigga.next