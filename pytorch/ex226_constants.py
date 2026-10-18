CHAR_LIM = 20
VOCAB = "abcdefghijklmnopqrstuvwxyz0123456789 .,!?'-_"
VOCAB_SIZE = len(VOCAB)
CHAR_TO_IX = {c: i for i, c in enumerate(VOCAB)}

input_data_fn = "dataset-ex226.txt"
device_name = "cuda"
model_fn = "model-ex226.pth"
