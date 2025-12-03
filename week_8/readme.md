

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.8.0-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/hair-type-classification)
[![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/yourusername/hair-type-classification)
# Hair Type Classification with CNN

A PyTorch implementation of a Convolutional Neural Network (CNN) for classifying hair types (straight vs curly) from images.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PyTorch 2.8.0+
- torchvision
- CUDA (optional, for GPU acceleration)

### Installation

# Clone the repository
git clone https://github.com/yourusername/hair-type-classification.git
cd hair-type-classification

# Install dependencies
pip install torch torchvision numpy matplotlib tqdm
Usage
python
# Run the complete pipeline
python train.py
📊 Dataset
Source: Kaggle Hair Type dataset (rebuilt)

Classes: Straight (0) vs Curly (1)

Train Images: ~1000

Test Images: ~200

Input Size: 3x200x200 (RGB)

🏗️ Model Architecture
text
CNN(
  (conv1): Conv2d(3, 32, kernel_size=3, stride=1)
  (relu): ReLU()
  (pool): MaxPool2d(kernel_size=2, stride=2)
  (fc1): Linear(313632, 64)
  (fc2): Linear(64, 1)
)
Parameters: 11,214,912

Loss Function: BCEWithLogitsLoss

Optimizer: SGD (lr=0.002, momentum=0.8)

📈 Results
Without Augmentation
Median Training Accuracy: ~0.84

Training Loss Std: ~0.078

With Augmentation
Mean Test Loss: ~0.08

Last 5 Epochs Test Accuracy: ~0.68

🔧 Data Augmentation
Random Rotation (±50°)

Random Resized Crop (200x200, scale 0.9-1.0)

Random Horizontal Flip
