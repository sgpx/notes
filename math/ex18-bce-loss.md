# binary cross entropy loss

for a neural network function approximation F(x) = Wh + B of a function y = f(x)

where h is the final output of several hidden layers S = activation_function(W_i*X + B_i)

if the true value is y_true and the prediction is y_pred

BCE = -(y_true*ln(y_pred) + (1-y_true)*(ln(1-y_pred))

if true value is y_true = 1 and prediction is y_pred = 0

BCE = -(1*ln(0)) + (1-1)*(ln(1)) = undefined

if y_true is 0.1 and y_pred is 0.99

BCE = -(0.1*ln(0.99) + (1-0.1)*(ln(0.01))

BCE = -(0.1*-0.01 + (1-0.1)*ln(0.01))

BCE = -(-0.0001 + 0.9*-4.6)

BCE = -(-4.14 - 0.0001) ~= 4.1455
