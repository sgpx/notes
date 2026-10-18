const OpenAI = require("openai");
const openai = new OpenAI.OpenAI();
const defaultModel = "gpt-4o-mini";

const converse = async (messages = [], model = defaultModel) => {
  const chatCompletion = await openai.chat.completions.create({
    messages: messages,
    model: defaultModel,
    temperature: 1,
  });

  const resp = chatCompletion?.choices[0]?.message?.content;
  return resp;
};

const invoke = (prompt = "", model = defaultModel) =>
  converse([{ role: "user", content: prompt }], model);

module.exports = { invoke, converse };
