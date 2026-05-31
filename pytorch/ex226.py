import torch
from torch.utils.data import Dataset, DataLoader

fn = "dataset-ex226.txt"

with open(fn, "r") as fr:
	raw = fr.read()

vocab = "abcdefghijklmnopqrstuvwxyz0123456789 .,!?'-_"
char_to_ix = {c: i+1 for i, c in enumerate(vocab)}
char_to_ix['<PAD>'] = 0	


lendist  = {}

def getrange(x):
    if x < 0:
        return "negative"
    for start in range(0, 1200, 100):
        end = start + 100
        if start <= x < end:
            return f"{start}-{end}"
    if 1200 <= x < 1300:
        return "1200-1300"
    return "1200+"

def process_line(i):
	lendist[getrange(len(i))] = lendist.get(getrange(len(i)), 0) + 1
	z = []
	uarr = []
	for j in i:
		uarr.append(1 if j.isupper() else 0)
		j = j.lower()
		if j not in vocab:
			z.append(0)
		else:
			z.append(char_to_ix[j])
	#print(i,z,uarr)
	return [z, uarr]
	
lines = [process_line(i) for i in raw.split("\n")]
print(lendist)
