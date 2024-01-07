function flatten(a){
    if(a.length > 0) {
        let p1 = a[0];
        let p2 = a.slice(1);
        if(Array.isArray(p1)) {
            return flatten(p1).concat(flatten(p2));
        }
        else {
            let tmp = [p1];
            return tmp.concat(flatten(p2));
        }
    }
    else {
        return a;
    }
}
