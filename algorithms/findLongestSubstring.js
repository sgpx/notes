function findLongestSubstring(a) {
  let sublen = 0,
    charObj = {};
  let s = 0,
    i = 0,
    acc = "";

  let isUnique = true;

  while (s < a.length) {
    let char = a[i];
    charObj[char] = (charObj[char] || 0) + 1;
    if (charObj[char] > 1) {
      isUnique = false;
    }
    console.log(charObj);
    acc += a[i];

    if (isUnique) {
      sublen = sublen > acc.length ? sublen : acc.length;
    }

    console.log(acc, i, a[i], s);
    i += 1;
    if (i === a.length) {
      s += 1;
      i = s;
      acc = "";
      isUnique = true;
      charObj = {};
    }
  }

  console.log(sublen, charObj);
  return sublen;
}

