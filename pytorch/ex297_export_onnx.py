#!/usr/bin/env python3
import io
import os
import sys
import warnings
import torch
import onnx
from model import SimpleNN

warnings.filterwarnings("ignore")

WEIGHTS_FILE = "ex297.pth"
ONNX_MODEL_FILE = "ex297.onnx"
ONNX_DATA_FILE = "ex297.onnx.data"


def export():
    # 1. Initialize model
    model = SimpleNN()

    weights_path = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].endswith(".pth") else WEIGHTS_FILE

    if os.path.exists(weights_path):
        print(f"Loading weights from {weights_path}...")
        state_dict = torch.load(weights_path, map_location="cpu", weights_only=True)
        model.load_state_dict(state_dict)
    else:
        print(f"Warning: Weights file '{weights_path}' not found, exporting with uninitialized weights.")

    model.eval()

    # 2. Create dummy input matching embedding dimension (1536)
    dummy_input = torch.randn(1, 1536, dtype=torch.float32)

    # 3. Export to ONNX buffer
    print("Exporting PyTorch model to ONNX...")
    onnx_buffer = io.BytesIO()
    torch.onnx.export(
        model,
        dummy_input,
        onnx_buffer,
        export_params=True,
        opset_version=17,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={
            "input": {0: "batch_size"},
            "output": {0: "batch_size"},
        },
        dynamo=False,
    )
    onnx_buffer.seek(0)
    model_proto = onnx.load_model_from_string(onnx_buffer.read())

    # 4. Remove existing target files if present to avoid FileExistsError
    for path in (ONNX_MODEL_FILE, ONNX_DATA_FILE):
        if os.path.exists(path):
            os.remove(path)

    # 5. Save model with external weights data
    print(f"Saving ONNX model to {ONNX_MODEL_FILE} and external data to {ONNX_DATA_FILE}...")
    onnx.save_model(
        model_proto,
        ONNX_MODEL_FILE,
        save_as_external_data=True,
        all_tensors_to_one_file=True,
        location=ONNX_DATA_FILE,
        size_threshold=1024,
        convert_attribute=False,
    )

    # 6. Validate the exported ONNX model
    onnx.checker.check_model(ONNX_MODEL_FILE)
    print("ONNX model structure validated successfully.")

    # 7. Test inference with ONNX Runtime if available
    try:
        import onnxruntime as ort
        import numpy as np

        session = ort.InferenceSession(ONNX_MODEL_FILE)
        input_name = session.get_inputs()[0].name
        test_input = dummy_input.numpy()
        onnx_outputs = session.run(None, {input_name: test_input})
        with torch.no_grad():
            torch_outputs = model(dummy_input).numpy()

        diff = np.max(np.abs(torch_outputs - onnx_outputs[0]))
        print(f"ONNX Runtime inference test passed. Max absolute difference vs PyTorch: {diff:.6e}")
    except Exception as e:
        print(f"Note: ONNX Runtime verification skipped ({e})")

    print(f"Export complete: '{ONNX_MODEL_FILE}' and '{ONNX_DATA_FILE}' generated.")


if __name__ == "__main__":
    export()
