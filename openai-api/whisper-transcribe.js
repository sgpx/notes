const fs = require('fs');
const OpenAI = require('openai');

const oaikey = fs.readFileSync("/tmp/oaikey.txt").toString().trim();
const openai = new OpenAI({apiKey: oaikey});

async function main() {
  const transcription = await openai.audio.transcriptions.create({
    file: fs.createReadStream("a.mp3"),
    model: "whisper-1",
  });
	console.log(transcription);
  console.log(transcription.text);
}
main();
