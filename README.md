# TechTown Smartphone Classifier

Welcome to the **TechTown Smartphone Classifier**, a machine learning application designed to classify smartphone brands—Brand A and Brand B—based on screen size and battery life. This project demonstrates the use of a logistic regression model, deployed with Streamlit, and includes an interactive visualization with a scatter plot distribution tailored to match a referenced fish project’s visual style, with a y-axis range adjusted to -5 to 6.

## Overview

This project is inspired by a fictional tech hub, TechTown, where engineers study two smartphone brands:
- **Brand A** (target = 0, represented by blue dots): Typically smaller screens and shorter battery life.
- **Brand B** (target = 1, represented by red dots): Typically larger screens and longer battery life.

The application uses a synthetic dataset with two features:
- `screen_size` (scaled inches): Negative values indicate smaller screens, positive values indicate larger screens.
- `battery_life` (scaled hours): Lower values indicate shorter battery life, higher values indicate longer battery life.

Due to overlap in the mid-range of screen size and battery life, the logistic regression model achieves an accuracy typically around 85–90%, reflecting the complexity of distinguishing brands based on these features alone.

## Features
- Generate a synthetic dataset with a scatter plot distribution matching the referenced fish project (dense clusters with overlap in the middle).
- Train a logistic regression model and evaluate its performance with accuracy, precision, recall, and F1-score.
- Interactive Streamlit app with a styled frontend to input `screen_size` and `battery_life` for real-time predictions.
- Visualization of the dataset with a scatter plot, including a decision boundary and user input point, with a y-axis range set to -5 to 6.

## Prerequisites
- Python 3.7 or higher
- Git (for version control)

![{D09ECF06-A899-4B4A-B11F-86E6E8FB52E3}](https://github.com/user-attachments/assets/f4570011-8906-4d26-89fe-d710d99e32f9)


  ![{39137E8F-C47C-4D3D-8D09-22E2F63F0B07}](https://github.com/user-attachments/assets/871900f7-4277-4b2b-8c17-9dddcea822c0)


  ![{0C220410-0C08-4D14-8F7A-C15629C5AD21}](https://github.com/user-attachments/assets/19dfb242-3b83-4408-889e-228845612f5d)

