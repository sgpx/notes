const isPalindrome = x => (x.length >= 2) ? x[0] === x[x.length-1] && isPalindrome(x.substring(1,x.length-1)) : true;
