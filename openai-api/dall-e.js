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
  console.log(await generateImage("icon for a job posting website called ReferJob.io. the icon should be a simple white solid colosky blue letters R and J arranged creatively on a sky blue background"));
};

main();
