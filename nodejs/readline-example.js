const readline = require("readline/promises");

async function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdin,
  });

  for (let i = 0; i < 5; i++) {
    const answer = await rl.question("enter text: ");
    console.log(`text was ${answer}`);
  }
  rl.close();
}

main();
