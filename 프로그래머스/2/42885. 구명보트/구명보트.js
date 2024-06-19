function solution(people, limit) {
  people.sort((a, b) => a - b);

  let boatCount = 0;
  let lightest = 0;
  let heaviest = people.length - 1;

  while (lightest <= heaviest) {
    let currentWeight = people[heaviest];
    heaviest--;

    if (currentWeight + people[lightest] <= limit) {
      currentWeight += people[lightest];
      lightest++;
    }

    boatCount++;
  }

  return boatCount;
}
