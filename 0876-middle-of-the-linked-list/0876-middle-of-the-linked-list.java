/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int size=0;
        ListNode curr=head;
        while (curr!=null){
            size++;
            curr=curr.next;
        }
        size=size/2;
        int size1=0;
        ListNode curr1=head;
        while (size1!=size){
            curr1=curr1.next;
            size1++;
        }
        return curr1;
    }
}