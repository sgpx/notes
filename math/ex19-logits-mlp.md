# logits for a 3 layer MLP and relu activation function for 3 class prediction 

input layer -> hidden layer -> activation function (relu) -> hidden layer -> output layer
IL -> HL1 ->  relu -> HL2 -> OL

let y = f(x) for the function f being approximated

the approximation is Z = F(h) + B

where h is the final result of all hidden layers post activation 

let number of input neurons = 15

let IL = nn.Linear(15,10), HL1 = nn.Linear(10,7), HL2 = nn.Linear(7,5), relu = nn.ReLU(), OL = nn.Linear(5,3)

IL = [X1 ... X15] -> [N1 ... N10]

S_1 = relu(W_1*X_input + B_1)

W_1 = [w_0 .... w_i]

the output is the logit vector Z = [Z_1 Z_2 Z_3]

logits are converted to probability by using

P = [P_0 ... P_k]

where P_i = e^Z_i / summation(j=0->k)(e^z_j)
