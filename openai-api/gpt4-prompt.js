const OpenAI = require("openai");
const fs = require("fs");
const rf = x => fs.readFileSync(x).toString().trim();

//const model = "gpt-4-0125-preview";
const model = "gpt-4";
const apikey = rf("/tmp/apikey.txt");
const prompt = rf("/tmp/prog/gpt4/a.txt");

const openai = new OpenAI({
  apiKey: apikey,
});

async function main() {
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: "user", content: prompt }],
    model,
  });
  console.log(chatCompletion?.choices[0]?.message?.content);
  const ts = new Date().getTime();
  console.log(`/tmp/prog/gpt4/response-${ts}.txt`); // , JSON.stringify(chatCompletion));
  fs.writeFileSync(`/tmp/prog/gpt4/response-${ts}.txt`, JSON.stringify(chatCompletion));
}

main();
