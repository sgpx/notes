const {
  InvokeModelCommand,
  BedrockRuntimeClient,
} = require("@aws-sdk/client-bedrock-runtime");
const fs = require("fs");

const main = async () => {
  const modelId = "ai21.jamba-instruct-v1:0";
  const prompt = fs.readFileSync("./prompt.txt").toString().trim();
  const client = new BedrockRuntimeClient({ region: "us-east-1" });
  const cmd = new InvokeModelCommand({
    modelId,
    body: JSON.stringify({
      messages: [{ role: "user", content: prompt }],
      n: 1,
    }),
  });
  const res = await client.send(cmd);
  const decodedResponseBody = new TextDecoder().decode(res.body);
  const responseBody = JSON.parse(decodedResponseBody);
  console.log(responseBody.choices[0].message.content);
};

main();
