#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
invoke.py

A tiny inference script that:
  * loads a saved LetterCNN checkpoint (model-ex288.pth)
  * builds the same model definition as used for training
  * loads the same image‑pre‑processing pipeline
  * returns a binary decision – “Letter present” or “No letters”.

Usage
-----
    python invoke.py /path/to/image.png

The script prints a short human‑readable verdict and also returns the
raw probability (0‑1) so you can set your own threshold if desired.
"""

import argparse
import pathlib
from typing import Tuple

import torch
import torch.nn as nn
from PIL import Image
from model import LetterCNN, build_preprocess_transform

def load_model(checkpoint_path: pathlib.Path, device: torch.device) -> Tuple[nn.Module, torch.device]:
    """
    Instantiates ``LetterCNN``, moves it to *device* and loads the weights
    stored in *checkpoint_path*.
    """
    model = LetterCNN().to(device)
    # ``map_location`` ensures the checkpoint loads onto the correct device
    checkpoint = torch.load(checkpoint_path, map_location=device)
    # The checkpoint was saved with ``torch.save(model.state_dict(), ...)``
    model.load_state_dict(checkpoint)
    model.eval()
    return model, device


_preprocess = build_preprocess_transform()


def predict_letter(image_path: pathlib.Path,
                   model: nn.Module,
                   device: torch.device,
                   threshold: float = 0.5) -> Tuple[str, float]:
    """
    Return a human‑readable decision and the raw probability that the image
    contains at least one English letter.

    Parameters
    ----------
    image_path: pathlib.Path
        Path to the image you want to classify.
    model: nn.Module
        The already‑loaded LetterCNN model (must be in eval mode).
    device: torch.device
        Device on which the model runs.
    threshold: float, optional
        Decision threshold (default 0.5).  Probabilities ≥ threshold → “Letter”.

    Returns
    -------
    decision: str
        Either ``"Letter detected"`` or ``"No letters"``.
    prob: float
        The raw network output before thresholding (range 0‑1 if you apply
        sigmoid manually; the network returns a logit, so we convert it
        to a probability here).
    """
    # ----------- 4.1 Load & preprocess the image --------------------
    img = Image.open(image_path).convert("RGB")
    input_tensor = _preprocess(img).unsqueeze(0)   # shape (1, 3, 224, 224)
    input_tensor = input_tensor.to(device)

    # ----------- 4.2 Forward pass ----------------------------------
    with torch.no_grad():
        logit = model(input_tensor)                # shape (1,)
        # Convert logit → probability with sigmoid
        prob = torch.sigmoid(logit).item()

    # ----------- 4.3 Decision ---------------------------------------
    decision = "Letter detected" if prob >= threshold else "No letters"
    return decision, prob


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Load a saved LetterCNN checkpoint and decide if an image "
                    "contains English letters (A‑Z, a‑z)."
    )
    parser.add_argument(
        "image_path",
        type=pathlib.Path,
        help="Path to the image you want to classify."
    )
    parser.add_argument(
        "--ckpt",
        type=pathlib.Path,
        default="model-ex288.pth",
        help="Path to the checkpoint file (default: model-ex288.pth)."
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
        help="Probability threshold for deciding ‘Letter detected’ (default: 0.5)."
    )
    args = parser.parse_args()

    # Determine device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Running inference on {device}")

    # Load model
    model, _ = load_model(args.ckpt, device)

    # Run inference
    decision, prob = predict_letter(args.image_path, model, device, args.threshold)

    # Print result
    print(f"\n=== Inference result for '{args.image_path.name}' ===")
    print(f"Probability of containing letters : {prob:.4f}")
    print(f"Decision                           : {decision}")
    print(f"Threshold used                     : {args.threshold}")


if __name__ == "__main__":
    main()
