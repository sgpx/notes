import { ElevenLabsClient } from "elevenlabs";
import * as fs from "fs";

const client = new ElevenLabsClient({
  apiKey: "sk_870a148cf2f8994b6603bf58466da95608d861e80636b31c",
});
const res = await client.speechToText.convert({
  file: fs.createReadStream("./a2.mp3"),
  model_id: "scribe_v1",
  num_speakers: 2,
  diarize: true,
});

console.log(res);

