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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  const dummyNode = new ListNode(0, head);
  let [slowPointer, fastPointer] = [dummyNode, head];

  while (fastPointer && n > 0) {
    fastPointer = fastPointer.next;
    n -= 1;
  }

  while (fastPointer) {
    slowPointer = slowPointer.next;
    fastPointer = fastPointer.next;
  }

  slowPointer.next = slowPointer.next.next;

  return dummyNode.next;
};
