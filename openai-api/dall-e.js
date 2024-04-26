const openai = require("openai");
if (!process.env.OPENAI_API_KEY) {
  throw Error("OpenAI API Key Not Loaded");
}
const clientOpenAI = new openai.OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const generateImage = async (prompt) => {
  const res = await clientOpenAI.images.generate({
    prompt,
    model: "dall-e-3",
    n: 1,
    size: "1024x1024",
  });
  return res?.data?.[0].url;
};

const main = async () => {
	console.log(await generateImage("logo for a website"));
};

main();
