<div align="center">
  <h1> Project Title: Newswires Classification</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/khatoonintech/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  

<sub>Project by:
<a href="https://www.linkedin.com/in/Khatoonintech/" target="_blank">Ayesha Noreen</a><br>
<small> Final Project @ByteWise </small>
</sub>

</div>

[<< Jupyter Notebook](../Final_Project/Newswires_Classification_with_DNN,RNN,and_BERT.ipynb) | [ Requirements >>](../Final_Project/requirement.txt)

<div align="center">
 
  ![newswires](../Final_Project/images/news.png)

</div>

## Overview

This project focuses on classifying newswires into different categories using the Reuters Newswires dataset, a collection of 11,228 news articles from 1986. The project uses a neural network implemented with TensorFlow and Keras, leveraging NLP techniques for feature extraction and classification. Key results include the model's accuracy in predicting the newswire categories, along with metrics such as precision, recall, and F1-score.

## Table of Contents

- [Overview](#overview)
- [System Setup](#system-setup)
- [Virtual Environment](#virtual-environment)
- [Installation of Dependencies](#installation-of-dependencies)
- [Running the Code](#running-the-code)
- [Reproducing Results](#reproducing-results)
- [Dataset](#dataset)
- [Key Results](#key-results)
- [License](#license)

## System Setup

### 1. Fork or Download the Code

You can either **fork** this repository to your own GitHub account or download the code directly to your local machine:

- To fork, click the "Fork" button at the top right of this repository on GitHub.
- To download:
  - Click the green **Code** button.
  - Select **Download ZIP** or clone the repository using Git:

  ```bash
  git clone https://github.com/yourusername/your-repository.git
  ```

### 2. Navigate to the Project Directory

Once the repository is cloned or downloaded, navigate to the project folder in your terminal:

```bash
cd your-repository
```

## Virtual Environment

### 1. Create a Virtual Environment

To ensure that all dependencies are installed consistently across systems, it's highly recommended to create a Python virtual environment.

- Create a virtual environment using the following command:

  ```bash
  python -m venv venv
  ```

  This creates a new directory named `venv` which holds the virtual environment.

### 2. Activate the Virtual Environment

- On **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

You should see your terminal change to show `(venv)` at the start of the prompt.

## Installation of Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

This will ensure all the necessary Python packages are installed, including TensorFlow, Keras, Sklearn, NLTK, Transformers, and other key libraries.

## Running the Code

### 1. Jupyter Notebook

The project contains a Jupyter notebook for ease of experimentation and visualization. To run the notebook, follow these steps:

1. Make sure `jupyter` is installed:

   ```bash
   pip install jupyter
   ```

2. Launch the notebook with the following command:

   ```bash
   jupyter notebook
   ```

3. Once the notebook opens in your web browser, navigate to `newswires_classification.ipynb` and run the cells to execute the project.

## Reproducing Results

To reproduce the results from the project, follow these steps:

1. Set up the environment as mentioned in [Virtual Environment](#virtual-environment) and [Installation of Dependencies](#installation-of-dependencies).
2. Run the Jupyter notebook by following the instructions in [Running the Code](#running-the-code).
3. Ensure the dataset is correctly loaded as per the instructions in the notebook.



## Dataset

The project uses the Reuters Newswires dataset, which contains:

- **Dataset Overview**: 11,228 newswires from Reuters, published in 1986.
- **Dataset Split**: 8,982 training samples, 2,246 test samples.
- **Categories**: 46 distinct categories.

This dataset can be loaded directly using Keras as follows:

```python
from keras.datasets import reuters
(X_train, Y_train), (X_test, Y_test) = reuters.load_data()
```

The data is automatically downloaded from the Keras datasets API. No manual download is required.

## Key Results

- **Accuracy**: 96.567%


## License

This project is not licensed yet.

## **Contact**
For any issues or inquiries, please contact 
- [LinkedIn](https://www.linkedin.com/in/khatoonintech)
- [Email](ayeshanoreen092@gmail.com)

