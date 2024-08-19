<div align="center">
  <h1> **Shakespeare Text Generation using RNN Models** </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/khatoonintech/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  

<sub>Created by:
<a href="https://www.linkedin.com/in/Khatoonintech/" target="_blank">Ayesha Noreen</a><br>
<small> ByteWiseLtd Fellowship : Week 10 </small>
</sub>

</div>


## **Introduction**

This project implements various Recurrent Neural Network (RNN) architectures to generate Shakespeare-like text. It explores simple RNN, bidirectional RNN, and a hybrid CNN-RNN model for text generation.

## Project Description

The project uses a dataset of Shakespeare's works to train different neural network models for text generation. It demonstrates the implementation and comparison of:

1. Simple RNN
2. Bidirectional RNN
3. Hybrid CNN-RNN model

Each model is trained to predict the next character in a sequence, allowing for the generation of new text in a style similar to Shakespeare's writings.

## Dependencies

This project requires the following Python libraries:

- numpy
- tensorflow
- keras

You can install these dependencies using pip:

```
pip install numpy tensorflow keras
```

## How to Run

1. Clone the repository to your local machine.
2. Ensure all dependencies are installed.
3. Run the Jupyter notebook or Python script containing the code.

The main steps in the project are:

1. Data preprocessing
2. Model creation (Simple RNN, Bidirectional RNN, Hybrid CNN-RNN)
3. Model training
4. Text generation

## File Structure

- `shakespeare_text_generation.ipynb`: Main Jupyter notebook containing all the code
- `README.md`: This file
- `shakespeare.txt`: Dataset file (will be downloaded automatically when running the code)

## Model Architectures

1. **Simple RNN**: A basic RNN model with multiple SimpleRNN layers.
2. **Bidirectional RNN**: An RNN model that processes sequences both forward and backward.
3. **Hybrid CNN-RNN**: A model that combines Convolutional Neural Network (CNN) layers with RNN layers.

## Text Generation

After training, you can generate text using the `generate_text` function. Example usage:

```python
generated_text = generate_text(model_name=model,
                               seed_text="You are all resolved rather to die than to famish?",
                               num_generated=100)
print(generated_text)
```

## Results

The README should include a brief summary of the results, comparing the performance and output quality of the different models.

## Future Improvements

- Experiment with different hyperparameters
- Try more advanced architectures like LSTM or Transformer models
- Use a larger dataset or fine-tune on specific Shakespeare plays

<sub>Contributor:

[Ayesha Noreen](https://www.linkedin.com/in/khatoonintech/)

<a href="https://www.linkedin.com/in/Khatoonintech/" target="_blank">Ayesha Noreen</a><br>
