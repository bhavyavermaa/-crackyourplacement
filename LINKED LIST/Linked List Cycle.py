"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
CODE 1:-
TWO POINTER APPROACH:-
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=head
        f=head
        while f and f.next:
            s= s.next
            f= f.next.next
            if s==f:
                return True
        return False
"""
Simple two pointer /slow-fast approach:-
1) Store head in two pointers
2) while we have not reached the end of the linked list
3) We increment the first pointer by 1 and second by 2
4) If we the elements are same, loop detected -> return True
5) End reached, No loop detected -> Return False
"""
CODE 2:-
ITERATIVE APPROACH:(FASTER METHOD)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        while curr:
            if curr.val is None:
                return True
            curr.val=None
            curr=curr.next
        return False

"""
We simply iterate through the linked list once.
1) Denote the head to a variable say curr
2) Iterate while the linked list has not end
3) Check is the val of the node is NONE and return True if it is.
4) Else update the value of the node to be NONE and update curr to the next element
