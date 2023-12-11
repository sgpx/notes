const fxn = (a, target) => {
  let tot = 0;
  let i = 0;
  let ns = 1;

  while (ns <= a.length) {
    console.log("i", i, "a[i]", a[i], "tot", tot, "ns", ns);
    tot += a[i];
    let tmp = i - ns;
    if (tmp >= 0) {
      tot -= a[i - ns];
    }
    if (tot >= target) {
      console.log(tot, ns);
      return ns;
    }
    i += 1;
    if (i === a.length) {
      i = 0;
      ns += 1;
      tot = 0;
    }
  }
  return 0;
};

