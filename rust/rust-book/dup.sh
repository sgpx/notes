node --eval 'process.chdir("arch"); 
const fs = require("fs"); 
const x = new Set(); 
fs.readdirSync(".").sort().forEach(fn => {
        const fc = fs.readFileSync(fn).toString();
        //console.log(`${fn}\n${fc}`);
        x.add(fc);
        fs.rmSync(fn);
})
Array.from(x).map((x,n) => {
    const n2 = n+1 < 10 ? `0${n+1}` : n+1;
    fs.writeFileSync(`u${n2}.rs`, x)
}); 
'
