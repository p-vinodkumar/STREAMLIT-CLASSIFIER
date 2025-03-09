import pandas as pd
from sklearn.datasets import make_classification

# Generate synthetic dataset to match the fish project's scatter plot
X, y = make_classification(n_samples=300, n_features=2, n_classes=2, 
                          n_informative=2, n_redundant=0, n_clusters_per_class=1, 
                          random_state=42, flip_y=0.1, class_sep=1.0)
df = pd.DataFrame(X, columns=["screen_size", "battery_life"])
df["target"] = y
df.to_csv("techtown_data.csv", index=False)