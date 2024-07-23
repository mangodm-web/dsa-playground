function removeDuplicates(s: string): string {
  const stack = [];

  for (const letter of s) {
    const popped = stack.pop() || "";
    
    if (letter !== popped) {
      stack.push(popped);
      stack.push(letter);
    }
  }

  return stack.join("");
};
