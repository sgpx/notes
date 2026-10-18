# LSTM

input of an LSTM consists of

- current input x_t
- previous hidden state h_t-1
- previous cell state c_t-1

for an LSTM, Y = F(X), Y must be a output state and X_i must be a sequence [x_i_1 x_i_2 ... ]

# gates

LSTMs use gates (smooth mechanisms ranging from 0 to 1) 

smooth mechanisms refers to the math functions used to create these gates

example: sigmoid function, tanh function

sigma(z) = 1/(1+e^-z)

# forget gate

decides what information to forget

f_t = sigma(W_f . [h_t-1, x_t] + b_f)

[h_t-1, x_t] is the concatentation operation and [] is the concat operator

# input gate

i_t = sigma(W_i . [h_t-1, x_t] + b_i)

C_tilde = tanh(W_c . [h_t, x_t] + b_c)

i_t is the input gate and C_tilde is the candidate cell state

# gate operations

- forget gate : decides what to discard from previous cell state
- input gate : decides what new info to add to cell state
- cell state update : applies the forget and input gates to cell state c_t
- output gate : decides what info from cell state to pass as hidden state

# weights

W_y, W_c, W_o, etc are the weight matrices that are updated during training

-----------------------------------------------------------------------------
W_f  | forget gate          | learns what info to discard from previous state
-----------------------------------------------------------------------------
W_i  | input gate           | learns what new information to keep from current input
-----------------------------------------------------------------------------
W_c  | candidate cell state | learns what candidate values to generate from [h_t-1, x_t]
-----------------------------------------------------------------------------
W_o  | output gate          | learns what cell state information to output as h_t
-----------------------------------------------------------------------------
W_y  | output layer         | learns how to transform final h_t into prediction Y
-----------------------------------------------------------------------------

# biases

b_f, b_i, b_c, b_o, b_y are bias vectors updated during training

-----------------------------------------------------------------------------
b_f | forget gate bias     | shifts activation threshold for forgetting info
-----------------------------------------------------------------------------
b_i | input gate bias      | shifts activation threshold for storing new info
-----------------------------------------------------------------------------
b_c | candidate state bias | shifts activation threshold for creating candidates
-----------------------------------------------------------------------------
b_o | output gate bias     | shifts activation threshold for emitting hidden state
-----------------------------------------------------------------------------
b_y | output layer bias    | shifts activation threshold for final linear transformation layer

# training

uses backpropagation through time (BPTT)

solves vanishing gradient problem in standard RNNs
	

