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
    public ListNode removeElements(ListNode head, int val) {
        while (head!=null && head.val==val){
            head=head.next;
        }
        if(head==null || head.next==null) return head;
        ListNode prev=head;
        ListNode curr=head.next;
        while(curr!=null){
            if (curr.val==val){
                prev.next=curr.next;
                curr=curr.next;
                continue;
            }
            curr=curr.next;
            prev=prev.next;
        }
        return head;
    }
}