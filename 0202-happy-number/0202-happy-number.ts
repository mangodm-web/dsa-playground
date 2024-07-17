function getSumSquares(n: number): number {
  let result = 0;

  while (n > 0) {
    const digit = n % 10;
    result += digit ** 2;
    n = Math.floor(n / 10);
  }

  return result;
}

function isHappy(n: number, checkedN = new Set<number>()): boolean {
  while (n !== 1 && !checkedN.has(n)) {
    checkedN.add(n);
    n = getSumSquares(n);
  }

  return n === 1;
}
