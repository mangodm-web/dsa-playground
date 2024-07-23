function reverseList(head: ListNode | null): ListNode | null {
  let cur = head;
  let prev = null;
  let next = null;

  while (cur) {
    next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }

  return prev;
};
