#include <stdio.h>
#include <math.h>

// ReLU
float relu(float x) {
    return x > 0 ? x : 0;
}

// Derivative of ReLU
float drelu(float x) {
    return x > 0 ? 1 : 0;
}

int main() {

    // Training data: learn y = 2x
    float x = 1.0;
    float y_true = 2.0;

    // Parameters (random init)
    float W1 = 0.5;
    float b1 = 0.0;
    float W2 = -0.3;
    float b2 = 0.0;

    float lr = 0.01;

    for (int epoch = 0; epoch < 1000; epoch++) {

        // ===== FORWARD PASS =====
        float z1 = W1 * x + b1;   // Linear 1
        float h  = relu(z1);      // Activation
        float pred = W2 * h + b2; // Linear 2

        float loss = pow(pred - y_true, 2);

        // ===== BACKWARD PASS =====

        // dL/dpred
        float dL_dpred = 2 * (pred - y_true);

        // pred = W2*h + b2
        float dpred_dW2 = h;
        float dpred_db2 = 1;
        float dpred_dh  = W2;

        // h = relu(z1)
        float dh_dz1 = drelu(z1);

        // z1 = W1*x + b1
        float dz1_dW1 = x;
        float dz1_db1 = 1;

        // Chain rule
        float dL_dW2 = dL_dpred * dpred_dW2;
        float dL_db2 = dL_dpred * dpred_db2;

        float dL_dz1 = dL_dpred * dpred_dh * dh_dz1;
        float dL_dW1 = dL_dz1 * dz1_dW1;
        float dL_db1 = dL_dz1 * dz1_db1;

        // ===== UPDATE =====
        W1 -= lr * dL_dW1;
        b1 -= lr * dL_db1;
        W2 -= lr * dL_dW2;
        b2 -= lr * dL_db2;

        if (epoch % 100 == 0) {
            printf("Epoch %d | Loss: %f | Pred: %f\n", epoch, loss, pred);
        }
    }

    printf("\nTrained params:\n");
    printf("W1=%f b1=%f W2=%f b2=%f\n", W1, b1, W2, b2);

    return 0;
}
