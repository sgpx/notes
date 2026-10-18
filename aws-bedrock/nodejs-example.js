const {
  BedrockRuntimeClient,
  InvokeModelCommand,
} = require("@aws-sdk/client-bedrock-runtime");
const runtime = new BedrockRuntimeClient({ region: "us-east-1" });

const prompt_j2u = async (prompt) => {
  const body = JSON.stringify({
    prompt,
    maxTokens: 8191,
  });
  const cmd = new InvokeModelCommand({
    modelId: "ai21.j2-ultra-v1",
    body,
    contentType: "application/json",
    accept: "application/json",
  });
  const ret = await runtime.send(cmd);
  const bodyStr = Buffer.from(ret.body);
  const responseData = JSON.parse(bodyStr);
  let output =
    responseData?.completions
      ?.map((y) => y?.data?.text)
      ?.filter(Boolean)
      ?.join("\n") || "";
  return output.trim();
};

const prompt_tg1 = async (prompt) => {
  const body = JSON.stringify({
    inputText: prompt.trim(),
    textGenerationConfig: { maxTokenCount: 4096 },
  });
  const cmd = new InvokeModelCommand({
    modelId: "amazon.titan-text-express-v1",
    body,
    contentType: "application/json",
    accept: "application/json",
  });
  const ret = await runtime.send(cmd);
  const bodyStr = Buffer.from(ret.body);
  const responseData = JSON.parse(bodyStr);
  output = responseData?.results?.map((y) => y.outputText).join("\n") || "";
  return output.trim();
};

const myPrompt = "what is a dwarf planet? in 10 words or less";

async function main() {
  console.log("j2u", await prompt_j2u(myPrompt));
  console.log("tg1", await prompt_tg1(myPrompt));
}

main();
