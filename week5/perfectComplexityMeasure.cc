String getWeight(int i) {
  if (i <= 0) {
    return "no weight";
  }
  if (i < 10) {
    return "light";
  }
  if (i < 20) {
    return "medium";
  }
  if (i < 30) {
    return "heavy";
  }
  return "very heavy";
}

int sumOfNonPrimes(int limit) {
  int sum = 0;
  OUTER: for (int i = 0; i < limit; ++i) {
    if (i <= 2) {
      continue;
    }
    for (int j = 2; j < i; ++j) {
      if (i % j == 0) {
        continue OUTER;
      }
    }
    sum += i;
  }
}