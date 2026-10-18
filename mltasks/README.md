- r2 score is not applicable for binary classification tasks
- simple imputer should be applied before standard scaler

**ROC-AUC Score**:

- The Receiver Operating Characteristic Area Under Curve (ROC-AUC) score measures the area under the ROC curve, which is a plot of the true positive rate against the false positive rate.

   ```python
   from sklearn.metrics import roc_auc_score

   y_pred_prob = pipe.predict_proba(X_test)[:, 1]
   roc_auc = roc_auc_score(y_test, y_pred_prob)
   print(f'ROC-AUC Score: {roc_auc}')
   ```

**Log-Loss**:

- Logarithmic Loss quantifies the accuracy of a classifier by penalizing false classifications. It's used for calculating probabilities.

   ```python
   from sklearn.metrics import log_loss

   logloss = log_loss(y_test, y_pred_prob)
   print(f'Log Loss: {logloss}')
   ```
