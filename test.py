import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Sample data
data = {
    'Sample ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'True Label': [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    'Predicted Probability': [0.7, 0, 0.3, 0.6, 0, 0, 1, 0.8, 0.4, 0.2]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Extract true labels and predicted probabilities
y_true = df['True Label']
y_scores = df['Predicted Probability']

# Calculate the ROC curve
fpr, tpr, x = roc_curve(y_true, y_scores)

# Calculate the AUC (Area Under the Curve)
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

# Calculate Youden's J statistic
J = tpr - fpr
optimal_idx = np.argmax(J)
optimal_threshold = thresholds[optimal_idx]

print(f'Optimal Threshold: {optimal_threshold}')
