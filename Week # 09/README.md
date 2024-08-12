
# **for Cat vs. Dog Classification**
---
## Overview

This Jupyter Notebook provides a comprehensive guide for classifying images of cats and dogs using a Convolutional Neural Network (CNN). The notebook utilizes the Microsoft Cats vs. Dogs dataset and demonstrates data preprocessing, model building, training, and evaluation.

## Objectives

-   Load and preprocess the dataset.
-   Build a CNN model to classify images.
-   Evaluate model performance using various metrics.

## Getting Started

## Prerequisites

Ensure you have the following installed:

-   Python 3.x
-   Jupyter Notebook
-   Required libraries: TensorFlow, Keras, NumPy, Matplotlib, scikit-learn

You can install the required libraries using pip:

`bash`
```
`pip install tensorflow keras numpy matplotlib scikit-learn` 
```
## Dataset

The dataset can be downloaded from Kaggle. You will need to create a Kaggle account and generate an API token (`kaggle.json`). Follow these steps:

1.  Create a directory named `kaggle` in your working directory.
2.  Place the `kaggle.json` file inside the `kaggle` directory.
3.  Use the following command to download the dataset:

python

`!kaggle datasets download -d shaunthesheep/microsoft-catsvsdogs-dataset` 

## Data Preparation

1.  **Extract the Dataset**: After downloading, extract the ZIP file to access the images.
2.  **Create Directory Structure**: Organize the images into training and testing directories:
    
    -   `Cats-vs-Dogs/Train/Cats`
    -   `Cats-vs-Dogs/Train/Dogs`
    -   `Cats-vs-Dogs/Test/Cats`
    -   `Cats-vs-Dogs/Test/Dogs`
    
3.  **Split the Dataset**: The notebook includes functions to split the dataset into training and testing sets, ensuring a balanced distribution of images.

## Data Augmentation

Use Keras's `ImageDataGenerator` to augment the training images. This step helps improve model generalization by applying random transformations such as:

-   Rescaling pixel values
-   Shearing
-   Zooming
-   Horizontal flipping

## Model Building

1.  **Define the Model Architecture**: The CNN model is built using Keras, consisting of convolutional layers, pooling layers, and fully connected layers.
2.  **Compile the Model**: The model is compiled with the Adam optimizer and binary cross-entropy loss function.
3.  **Train the Model**: Fit the model on the training data and evaluate its performance on the testing data.

## Callbacks

Utilize the following callbacks to enhance the training process:

-   **ModelCheckpoint**: Save the best model based on validation accuracy.
-   **EarlyStopping**: Stop training when validation loss stops improving to prevent overfitting.

## Model Evaluation

Evaluate the model's performance using:

-   Accuracy
-   Confusion Matrix
-   Classification Report (Precision, Recall, F1-Score)

## Running the Notebook

1.  Open the Jupyter Notebook in your preferred environment.
2.  Follow the steps outlined in each section to load the dataset, preprocess the images, build the model, and evaluate its performance.
3.  Visualize the results and make any adjustments as needed.

## Conclusion

This notebook provides a foundational approach to image classification using CNNs. You can further enhance the model by experimenting with different architectures, hyperparameters, and additional data augmentation techniques.
