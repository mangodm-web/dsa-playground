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
  let currentNode = new ListNode();
  const dummyNode = currentNode;

  while (list1 && list2) {
    if (list1.val > list2.val) {
      currentNode.next = list2;
      list2 = list2.next;
    } else {
      currentNode.next = list1;
      list1 = list1.next;
    }

    currentNode = currentNode.next;
  }

  if (list1) {
    currentNode.next = list1;
  }

  if (list2) {
    currentNode.next = list2;
  }

  return dummyNode.next;
};
