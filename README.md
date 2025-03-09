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

  Dataset story

  Imagine a bustling tech hub called TechTown, known for its innovative smartphone manufacturing. Two leading brands dominate the market: Brand A (represented by blue dots) and Brand B (represented by red dots). Engineers in TechTown are analyzing smartphone data to optimize production and assist retailers in stocking the right models.

The scatter plot from their analysis plots screen_size (in inches, scaled on the x-axis) against battery_life (in hours, scaled on the y-axis). Lower screen_size values indicate smaller screens, while higher values indicate larger screens. Lower battery_life values signify shorter battery durations, and higher values indicate longer battery life.

The engineers collected data on hundreds of smartphone models, labeling each as either Brand A (target 0, blue) or Brand B (target 1, red). Their goal was to predict the brand using only screen size and battery life, helping retailers predict demand.

However, the plot reveals a varied distribution. Brand A models tend to have smaller screens and shorter battery life (more blue dots on the left and lower parts), while Brand B models feature larger screens and longer battery life (more red dots on the right and upper parts). Yet, there’s noticeable overlap in the middle, where mid-sized screens and average battery life could belong to either brand, complicating predictions.

This overlap suggests that screen size and battery life alone may not fully distinguish the brands. Factors like price, camera quality, or processor speed might also influence classification. The engineers may need more data or a more sophisticated model to enhance accuracy.

For TechTown retailers, this means they can’t rely solely on rules like “larger screens mean Brand B.” Collaboration with engineers is key to refining prediction models or adjusting inventory strategies. For now, this scatter plot illustrates the diverse nature of smartphone design, where two key metrics reveal a complex market landscape.

Under the guidance of [ Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)
