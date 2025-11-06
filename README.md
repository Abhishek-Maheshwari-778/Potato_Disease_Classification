# 🥔 Potato Disease Classification

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success?style=flat-square)](https://github.com/Abhishek-Maheshwari-778/Potato_Disease_Classification)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.114%2B-teal?style=flat-square)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.35%2B-red?style=flat-square)](https://streamlit.io/)
[![TensorFlow](https://img.shields.io/badge/tensorflow-2.10%2B-orange?style=flat-square)](https://www.tensorflow.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

### 🌱 AI-Powered Potato Leaf Disease Detection
**Detect potato leaf diseases with 95%+ accuracy using Deep Learning and CNN**

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Model Performance](#-model-performance)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [Team](#-team)
- [License](#-license)

---

## 🔍 Overview

This project implements a **Convolutional Neural Network (CNN)** to classify potato leaf diseases into three categories:
- ✅ **Healthy** - Disease-free potato leaves
- ⚠️ **Early Blight** - Caused by *Alternaria solani*
- 🚨 **Late Blight** - Caused by *Phytophthora infestans*

The system consists of:
- **Backend**: FastAPI server serving a trained Keras model
- **Frontend**: Modern Streamlit web interface
- **Model**: CNN trained on PlantVillage dataset with 95%+ accuracy

---

## ✨ Features

### 🎯 Core Functionality
- **Real-time Disease Detection**: Upload potato leaf images and get instant predictions
- **High Accuracy**: 95%+ classification accuracy using advanced CNN architecture
- **User-Friendly Interface**: Modern, responsive web design with Streamlit
- **Fast API**: Lightning-fast predictions with FastAPI backend

### 🔧 Technical Features
- **RESTful API**: Clean API endpoints for easy integration
- **CORS Enabled**: Cross-origin support for web applications
- **Error Handling**: Comprehensive error handling and validation
- **Model Management**: Automatic model loading and validation
- **Batch Processing**: Support for multiple image uploads
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### 📊 Visualization
- **Confidence Scores**: Detailed prediction confidence percentages
- **Progress Indicators**: Visual feedback during analysis
- **Sample Images**: Reference images for each disease type
- **Interactive Charts**: Beautiful UI with custom styling

---

## 🎥 Demo

### Quick Start (Windows)
```bash
# One-click launcher - starts both backend and frontend
start_app.bat
```

### Manual Setup
```bash
# Terminal 1: Start Backend
cd api
pip install -r requirements.txt
python main.py

# Terminal 2: Start Frontend  
cd website
pip install -r requirements.txt
streamlit run app.py
```

**Access Points:**
- 🌐 **Web Interface**: http://localhost:8501
- 🔌 **API Endpoint**: http://localhost:8000
- 📖 **API Docs**: http://localhost:8000/docs

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Windows/Linux/macOS

### Step 1: Clone the Repository
```bash
git clone https://github.com/Abhishek-Maheshwari-778/Potato_Disease_Classification.git
cd Potato_Disease_Classification
```

### Step 2: Set Up Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install API dependencies
cd api
pip install -r requirements.txt
cd ..

# Install frontend dependencies  
cd website
pip install -r requirements.txt
cd ..
```

### Step 4: Prepare the Model
1. Download the trained model `1.keras`
2. Place it in `training/models/` directory
3. Ensure the model path is correct in `api/main.py`

---

## 📖 Usage

### Method 1: One-Click Launcher (Windows)
```bash
# Double-click or run from command line
start_app.bat
```
This automatically:
- ✅ Starts FastAPI backend on port 8000
- ✅ Launches Streamlit frontend on port 8501  
- ✅ Opens web browser with the application

### Method 2: Manual Start
```bash
# Terminal 1 - Backend Server
cd api
python main.py

# Terminal 2 - Frontend (new terminal)
cd website  
streamlit run app.py
```

### Method 3: Using the API Directly
```python
import requests

# Upload image for prediction
with open('potato_leaf.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/predict', files=files)
    
result = response.json()
print(f"Disease: {result['class']}")
print(f"Confidence: {result['confidence']}%")
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Health Check
```http
GET /ping
```
**Response:**
```json
{
  "status": "active",
  "model_loaded": true
}
```

#### 2. Predict Disease
```http  
POST /predict
Content-Type: multipart/form-data
```
**Parameters:**
- `file` (required): Image file (JPG, PNG, JPEG)

**Response:**
```json
{
  "class": "Healthy",
  "confidence": 97.12
}
```

**Error Response:**
```json
{
  "error": "Model not loaded. Please check server logs."
}
```

#### 3. API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📈 Model Performance

### Dataset
- **Source**: PlantVillage Dataset
- **Total Images**: 4,000+ potato leaf images
- **Classes**: 3 (Healthy, Early Blight, Late Blight)
- **Split**: 80% Training, 20% Validation

### Architecture
- **Model Type**: Convolutional Neural Network (CNN)
- **Input Size**: 256x256 pixels
- **Layers**: 6 Convolutional + 3 Dense layers
- **Activation**: ReLU for hidden layers, Softmax for output
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy

### Results
| Metric | Score |
|--------|-------|
| **Accuracy** | 95.2% |
| **Precision** | 94.8% |
| **Recall** | 95.1% |
| **F1-Score** | 94.9% |

---

## 🏗️ Project Structure

```
Potato_Disease_Classification/
│
├── 📁 api/                          # FastAPI Backend
│   ├── 📄 main.py                   # Main API server
│   ├── 📄 requirements.txt          # Backend dependencies
│   └── 📁 models/                   # Trained models (gitignored)
│
├── 📁 website/                      # Streamlit Frontend  
│   ├── 📄 app.py                    # Main Streamlit app
│   ├── 📄 requirements.txt          # Frontend dependencies
│   └── 📁 images/                   # Sample disease images
│       ├── 🖼️ healthy.JPG
│       ├── 🖼️ early_blight.JPG
│       └── 🖼️ late_blight.JPG
│
├── 📁 training/                     # Model Training
│   ├── 📓 training.ipynb           # Jupyter notebook for training
│   ├── 📁 models/                   # Saved models (gitignored)
│   └── 📁 PlantVillage/             # Dataset (gitignored)
│
├── 🚀 start_app.bat                 # Windows launcher
├── 📄 README.md                     # This file
├── 📄 LICENSE                       # MIT License
└── 📄 .gitignore                    # Git ignore rules
```

---

## 🛠️ Tech Stack

### Core Technologies
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
</p>

### Dependencies
- **Deep Learning**: `tensorflow`, `keras`, `numpy`
- **Web Framework**: `fastapi`, `uvicorn` 
- **Frontend**: `streamlit`, `requests`
- **Image Processing**: `pillow`
- **Development**: `jupyter`, `notebook`

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👥 Team

### Development Team
| Name | Role | GitHub |
|------|------|--------|
| **Abhishek Maheshwari** | Project Lead & ML Engineer | [@Abhishek-Maheshwari-778](https://github.com/Abhishek-Maheshwari-778) |
| **Vaishnavi Gupta** | Frontend Developer | [@vaishnavi](https://github.com/vaishnavi) |
| **Prateek Gupta** | Backend Developer | [@prateek](https://github.com/prateek) |
| **Samina Nooreen** | UI/UX Designer | [@samina](https://github.com/samina) |
| **Soni** | Data Analyst | [@soni](https://github.com/soni) |
| **Purti Singh** | QA Engineer | [@purti](https://github.com/purti) |
| **Anishka Bhatt** | Documentation | [@anishka](https://github.com/anishka) |
| **Hemendra Gangwar** | DevOps Engineer | [@hemendra](https://github.com/hemendra) |

### Mentor
- **Vedant Sir** - Project Mentor and Guide

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PlantVillage Dataset** for providing the training data
- **FastAPI** team for the excellent web framework
- **Streamlit** team for the amazing frontend library
- **TensorFlow** team for the powerful ML framework
- Our mentor **Vedant Sir** for guidance and support

---

## 📞 Contact

For questions, suggestions, or collaboration opportunities:

📧 **Email**: abhishek.maheshwari@example.com
🔗 **LinkedIn**: [Abhishek Maheshwari](https://linkedin.com/in/abhishek-maheshwari)
🐙 **GitHub Issues**: [Create an Issue](https://github.com/Abhishek-Maheshwari-778/Potato_Disease_Classification/issues)

---

<div align="center">

### ⭐ If this project helped you, please give it a star!

**Made with ❤️ by Abhishek Maheshwari & Team**

</div>






