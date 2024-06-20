/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  const dummyNode = new ListNode();
  let current = dummyNode;

  let left = list1;
  let right = list2;
  
  while (left && right) {
    if (left.val > right.val) {
      current.next = right;
      right = right.next;
    } else {
      current.next = left;
      left = left.next;
    }
    current = current.next;
  }
  
  if (left) {
    current.next = left;
  }
  
  if (right) {
    current.next = right;
  }
  
  return dummyNode.next;
};
