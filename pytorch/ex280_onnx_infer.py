import os
import numpy as np
import onnxruntime as ort
import dotenv

dotenv.load_dotenv()

import llm

# ------------------------------------------------------------------
# 1️⃣  Load the ONNX model
# ------------------------------------------------------------------
ONNX_MODEL_PATH = "ex280.onnx"
if not os.path.isfile(ONNX_MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {ONNX_MODEL_PATH}")

# You can enable a specific execution provider if you have one installed,
# e.g. ort.get_device())   # 'CPUExecutionProvider', 'CUDAExecutionProvider', ...
session_opts = ort.SessionOptions()
session_opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
# session_opts.enable_mem_pattern = True           # optional tweaks
# session_opts.intra_op_num_threads = 4            # optional threading

# Create the inference session
session = ort.InferenceSession(ONNX_MODEL_PATH, sess_options=session_opts)

input_meta = session.get_inputs()
input_name = input_meta[0].name           # should be "input"
assert input_name == "input", "Unexpected input name!"

# ------------------------------------------------------------------
# 2️⃣  Run inference on sample song titles
# ------------------------------------------------------------------
sample_songs = [
    "Dear You - Higurashi no Naku Koro Ni",
    "Prince - When Doves Cry",
    "They Don't Care About Us",
    "MJ The Bad Tour",
    "You Shook Me All Night Long",
    "Forrest Gump",
    "Prince - 1999",
    "Social Distortion | Story of My Life",
    "Prince and the Revolution - Let's Go Crazy",
    "No Celebrity Could Stay Serious Around Prince!",
    "The Cure - Trust",
]

print("\n--- ONNX sample song title test ---")
for song_title in sample_songs:
    emb = llm.get_embedding(f"Media title: {song_title}")
    emb_np = np.asarray(emb, dtype=np.float32).reshape(1, -1)

    outputs = session.run(None, {input_name: emb_np})
    output_np = outputs[0]
    logit = float(output_np.item())
    probability = 1.0 / (1.0 + np.exp(-logit))
    prediction = "IS_MUSIC" if probability >= 0.5 else "NOT_MUSIC"

    print(f"{song_title} : {prediction} (logit={logit:.4f}, prob={probability:.4f})")
