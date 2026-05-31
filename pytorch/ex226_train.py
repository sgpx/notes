import torch
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch.optim as optim

from ex226_constants import (
	device_name,
	CHAR_LIM,
	CHAR_TO_IX,
	VOCAB_SIZE,
	input_data_fn,
	model_fn,
)
from ex226_model import FNN

with open(input_data_fn, "r", encoding="utf-8", errors="ignore") as fr:
	raw = fr.read()

allX, allY = [],[]

def encode_char(ch):
	vec = [0] * VOCAB_SIZE
	ix = CHAR_TO_IX.get(ch.lower())
	if ix is not None:
		vec[ix] = 1
	return vec

def process_line(i):
	if len(i) > CHAR_LIM:
		for s in range(0,len(i), CHAR_LIM):
			chunk = i[s:(s+CHAR_LIM)]
			process_line(chunk)
		return

	z = []
	uarr = []
	for j in i:
		uarr.append(1 if j.isupper() else 0)
		z.extend(encode_char(j))

	pad_chars = CHAR_LIM - len(i)
	if pad_chars > 0:
		z.extend([0] * (pad_chars * VOCAB_SIZE))
		uarr = uarr + ([0] * pad_chars)

	diff = CHAR_LIM - len(uarr)
	if diff > 0:
		uarr = uarr + ([0] * diff)
	if len(z) != CHAR_LIM * VOCAB_SIZE or len(uarr) != CHAR_LIM:
		print(len(z), len(uarr))
		exit(1)
	allX.append(z)
	allY.append(uarr)

import datetime

ts = lambda : datetime.datetime.now().strftime("%H:%M:%S")

print("Starting data preprocessing", ts())
for line in raw.split("\n"):
	process_line(line)

print("Completed data preprocessing", ts())
print("creating tensors", ts())
tX, tY = torch.tensor(allX, dtype=torch.float32, device=device_name), torch.tensor(allY, dtype=torch.float32, device=device_name)
print("created tensors", ts())
print("creating Dataset", ts())
data = torch.utils.data.TensorDataset(tX, tY)
print("created Dataset", ts())

test_size = int(0.2*len(data))
train_size = len(data) - test_size

print("creating split", ts())
train_dataset, test_dataset = random_split(data, [train_size, test_size])
print("created split", ts())

print("creating test loader", ts())
test_loader = DataLoader(test_dataset, batch_size=CHAR_LIM, shuffle=False)
print("created test loader", ts())

print("creating train loader", ts())
train_loader = DataLoader(train_dataset, batch_size=CHAR_LIM, shuffle=True)
print("created train loader", ts())

model = FNN().to(device_name)
pos_count = 6
neg_count = 10
weight_val = neg_count / pos_count 

criterion = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([weight_val], device=device_name))
optimizer = optim.Adam(model.parameters(), lr=0.01)

NUM_EPOCHS = 100
print("Starting training epochs", ts())
for epoch in range(NUM_EPOCHS):
	print("epoch", epoch)
	for x_batch, y_batch in train_loader:
		y_hat = model(x_batch)
		loss = criterion(y_hat, y_batch)
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

	

torch.save(model.state_dict(), model_fn)

with torch.no_grad():
    model.eval()

    tp = 0
    fp = 0
    input_data_fn = 0

    for x, y in test_loader:
        pred = model(x)
        pred = (pred > 0.0).float()

        tp += ((pred == 1) & (y == 1)).sum().item()
        fp += ((pred == 1) & (y == 0)).sum().item()
        input_data_fn += ((pred == 0) & (y == 1)).sum().item()

    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + input_data_fn + 1e-8)

    f1 = 2 * precision * recall / (precision + recall + 1e-8)

    print("precision:", precision)
    print("recall:", recall)
    print("f1:", f1)
