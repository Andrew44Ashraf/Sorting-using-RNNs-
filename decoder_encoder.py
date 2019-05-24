import numpy as np


def encode(X,seq_len, vocab_size):
    x = np.zeros((len(X),seq_len, vocab_size), dtype=np.float32)
    for ind,batch in enumerate(X):
        for j, elem in enumerate(batch):
            x[ind, j, elem] = 1
    return x


def batch_gen(batch_size=32, seq_len=10, max_no=100):
    
    x = np.zeros((batch_size, seq_len, max_no), dtype=np.float32)
    y = np.zeros((batch_size, seq_len, max_no), dtype=np.float32)

    while True:
	# Generates a batch of input
        X = np.random.randint(max_no, size=(batch_size, seq_len))

        Y = np.sort(X, axis=1)

        for ind,batch in enumerate(X):
            for j, elem in enumerate(batch):
                x[ind, j, elem] = 1

        for ind,batch in enumerate(Y):
            for j, elem in enumerate(batch):
                y[ind, j, elem] = 1

        yield x, y
        x.fill(0.0)
        y.fill(0.0)