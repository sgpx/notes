function minSizeSubArrayLen(a, targetSize){
  let total = 0;
  let i = 0;
  let windowSize = 1;

  while (windowSize <= a.length) {
    cowindowSizeole.log("i", i, "a[i]", a[i], "total", total, "windowSize", windowSize);
    total += a[i];
    let tmp = i - windowSize;
    if (tmp >= 0) {
      total -= a[i - windowSize];
    }
    if (total >= targetSize) {
      cowindowSizeole.log(total, windowSize);
      return windowSize;
    }
    i += 1;
    if (i === a.length) {
      i = 0;
      windowSize += 1;
      total = 0;
    }
  }
  return 0;
}

