function binarySearch(x,v){
    let l = 0, r = x.length - 1;
    if(x[l] === v) return l;
    if(x[r] === v) return r;
    
    let mid = parseInt((l+r) / 2);
    while(r-l > 1){
        if(x[mid] === v) return mid;
        else if(x[mid] < v) l = mid;
        else if(x[mid] > v) r = mid;
        mid = parseInt((l+r) / 2);
    }
    return -1;
}
