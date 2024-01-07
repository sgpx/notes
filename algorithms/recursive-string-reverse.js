const reverse = (s) => s.length > 0 ? s[s.length - 1] + reverse(s.substring(0,s.length-1)) : "";
