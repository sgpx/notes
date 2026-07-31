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
ONNX_DATA_PATH = "ex280.onnx.data"

if not os.path.isfile(ONNX_MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {ONNX_MODEL_PATH}")

if not os.path.isfile(ONNX_DATA_PATH):
    raise FileNotFoundError(f"Data file not found: {ONNX_DATA_PATH}")

# You can enable a specific execution provider if you have one installed,
# e.g. ort.get_device())   # 'CPUExecutionProvider', 'CUDAExecutionProvider', ...
session_opts = ort.SessionOptions()
session_opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
# session_opts.enable_mem_pattern = True           # optional tweaks
# session_opts.intra_op_num_threads = 4            # optional threading

# Create the inference session

def get_prediction(song_title : str):
    session = ort.InferenceSession(ONNX_MODEL_PATH, sess_options=session_opts)
    input_meta = session.get_inputs()
    input_name = input_meta[0].name           # should be "input"
    assert input_name == "input", "Unexpected input name!"
    emb = llm.get_embedding(f"Media title: {song_title}")
    emb_np = np.asarray(emb, dtype=np.float32).reshape(1, -1)
    outputs = session.run(None, {input_name: emb_np})
    output_np = outputs[0]
    logit = float(output_np.item())
    probability = 1.0 / (1.0 + np.exp(-logit))
    prediction = "IS_MUSIC" if probability >= 0.5 else "NOT_MUSIC"
    print(f"{song_title} : {prediction} (logit={logit:.4f}, prob={probability:.4f})")
    return prediction

def lambda_handler(event, context):
    input = event.get("body", "")
    result: str = get_prediction(input) if input else "INVALID_INPUT"
    return {"body": result, "statusCode": 200}
