import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("techtown_model.pkl")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #2c3e50;
        font-size: 36px;
        font-weight: bold;
        padding: 10px;
        background-color: #ecf0f1;
    }
    .sidebar .sidebar-content {
        background-color: #f5f6f5;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom styling
st.markdown('<div class="title">TechTown Smartphone Classifier</div>', unsafe_allow_html=True)

# Sidebar with enhanced layout
with st.sidebar:
    st.header("Device Features")
    st.write("Negative values = smaller/shorter, Positive = larger/longer")
    screen_size = st.slider("Screen Size (inches, scaled)", -5.0, 5.0, 0.0, key="screen")
    battery_life = st.slider("Battery Life (hours, scaled)", -5.0, 5.0, 0.0, key="battery")

# Prepare input for prediction
input_features = np.array([[screen_size, battery_life]])

# Prediction section
if st.button("Predict Brand", help="Click to predict the smartphone brand"):
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0]
    st.subheader("Prediction Results")
    st.write(f"**Predicted Brand:** {'Brand B' if prediction == 1 else 'Brand A'}")
    st.write(f"**Probability of Brand A:** {probability[0]:.2f}")
    st.write(f"**Probability of Brand B:** {probability[1]:.2f}")

# Optional data visualization
if st.checkbox("Show Data Visualization"):
    df = pd.read_csv("techtown_data.csv")
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = sns.scatterplot(x="screen_size", y="battery_life", hue="target", 
                              palette={0: "blue", 1: "red"}, s=80, alpha=0.6, data=df, ax=ax)
    ax.scatter(screen_size, battery_life, color="green", s=120, label="User Input", marker="x")
    
    # Plot decision boundary
    w = model.coef_[0]
    b = model.intercept_[0]
    x_range = np.linspace(-5, 5, 100)
    y_range = -(w[0] * x_range + b) / w[1]
    ax.plot(x_range, y_range, "k--", label="Decision Boundary", linewidth=1.5)
    
    # Custom legend handles and labels
    handles, labels = ax.get_legend_handles_labels()
    custom_handles = [
        plt.Line2D([0], [0], marker='o', color='blue', label='Brand A', markersize=10, linestyle=''),
        plt.Line2D([0], [0], marker='o', color='red', label='Brand B', markersize=10, linestyle=''),
        plt.Line2D([0], [0], marker='x', color='green', label='User Input', markersize=12, linestyle=''),
        plt.Line2D([0], [0], color='black', label='Decision Boundary', linestyle='--', linewidth=1.5)
    ]
    ax.legend(handles=custom_handles, labels=['Brand A', 'Brand B', 'User Input', 'Decision Boundary'], 
              loc='best', frameon=True, fontsize=10)
    
    # Add labels and title to plot
    ax.set_xlabel("Screen Size (scaled)")
    ax.set_ylabel("Battery Life (scaled)")
    ax.set_title("Smartphone Brand Distribution", pad=15)
    
    # Set y-axis limits to -5 to 6
    ax.set_ylim(-5, 6)
    
    st.pyplot(fig)