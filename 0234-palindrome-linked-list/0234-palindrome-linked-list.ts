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

function isPalindrome(head: ListNode | null): boolean {
  const array = [];
  let [left, right] = [head, head];

  while (right) {
    array.push(right.val);
    right = right.next;
  }
  
  for (let i = array.length - 1; i > 0; i--) {
    if (left.val !== array.pop()) {
      return false;
    }

    left = left.next;
  }

  return true;
};
