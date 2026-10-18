import React, { useState, useEffect, useRef } from "react";

type ExampleProps = {
  title: string;
};

const Example = ({ title }: ExampleProps) => {
  const [mediaRec, setMediaRec] = useState<MediaRecorder | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const [audioState, setAudioState] = useState<string | null>(
    null
  );
  const audioRef = useRef<HTMLAudioElement>(null);

  useEffect(() => {
    if (audioRef && audioRef.current && audioRef.current.play) {
      audioRef.current.play();
    }
  }, [audioState]);

  useEffect(() => {
    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        const mediaRecorder = new MediaRecorder(stream);
        setMediaRec(mediaRecorder);
      })
      .catch((e) => alert(`ERROR: ${e.toString()}`));
  }, []);

  const stopRecording = async () => {
    if (mediaRec) {
      mediaRec.stop();
      setIsRecording(false);
    }
  };

  const startRecording = async () => {
    setIsRecording(true);
    const chunks: any[] = [];
    if (mediaRec) {
      mediaRec.ondataavailable = (data) => chunks.push(data.data);
      mediaRec.onstop = () => {
        const blobAudio = new Blob(chunks, { type: "audio/wav; codecs=0" });
        const flr = new FileReader();
        flr.readAsDataURL(blobAudio);
        flr.onloadend = () => {
          if (flr?.result && typeof flr.result === "string") {
            setAudioState(flr.result);
          }
        };
      };
      mediaRec.start();
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-start",
        alignItems: "flex-start",
      }}
    >
      <div>
        <h4>Scenario : {title}</h4>
      </div>
      {!isRecording ? (
        <button
          onClick={startRecording}
          type="primary"
          disabled={isRecording}
        >
          Start Recording
        </button>
      ) : (
        <button onClick={stopRecording} type="primary" disabled={!isRecording}>
          Stop Recording
        </button>
      )}
      {audioState && (
        <audio
          ref={audioRef}
          src={audioState}
          style={{ display: "none" }}
        />
      )}
    </div>
  );
};

export default Example;
