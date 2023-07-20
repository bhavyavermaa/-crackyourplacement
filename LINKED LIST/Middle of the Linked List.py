"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""
CODE:-
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        double=single=head
        while double and double.next:
            single=single.next
            double=double.next.next
        return single
"""
APPROACH:- Two Pointer Approach
1) We initialize two pointers and denote their value to head.
    The two pointers are single and double.
    The name denote that single moves a single node and double moves double steps.
2) While we have not reached the end of the linked list and we denote it using double because it is moving at a speed twice than the single.
3) For every iteration, we move single one step and double two steps
    This means that when at n//2'th iteration single will reach the mid, double will reach the end. 
4) return the pointer single.
