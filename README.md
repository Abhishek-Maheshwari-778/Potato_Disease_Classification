# Potato Disease Classification

Detect potato leaf diseases (Healthy, Early Blight, Late Blight) using a CNN served via FastAPI with a modern Streamlit UI.

![Status Badge](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.114%2B-teal)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-red)

---

## Overview

- Predicts among three classes: `Healthy`, `Early Blight`, `Late Blight`.
- Backend: `FastAPI` that loads a trained Keras model and exposes `/predict`.
- Frontend: `Streamlit` app for uploading images and visualizing predictions.
- Trained on `PlantVillage` potato leaf dataset.

---

## Project Structure

```
potato-disease/
├── training/
│   ├── training.ipynb           # Notebook used to train the CNN model
│   ├── models/                  # Saved trained model(s)
│   │   └── 1.keras              # Example model file (ignored in VCS)
│   └── PlantVillage/            # Dataset (kept local, not tracked)
│
├── api/
│   ├── main.py                  # FastAPI backend for serving model predictions
│   └── requirements.txt         # Python dependencies for API
│
├── website/
│   ├── app.py                   # Streamlit UI
│   ├── images/
│   │   ├── healthy.jpg          # Sample image used in About section
│   │   ├── early_blight.jpg
│   │   └── late_blight.jpg
│   └── requirements.txt         # Python dependencies for UI
│
├── start_app.bat                # (Windows) launcher for backend and UI
└── README.md
```

---

## Quick Start

### 1) Prepare Python environment

- Use a virtual environment (`python -m venv .venv && .venv\Scripts\activate`) or Conda.

### 2) Start the API server

```
cd api
pip install -r requirements.txt
python main.py
```

- The API listens at `http://localhost:8000`.
- Ensure `training/models/1.keras` exists relative to repository root.

### 3) Start the Streamlit frontend

Open a new terminal:

```
cd website
pip install -r requirements.txt
streamlit run app.py
```

- The UI opens at `http://localhost:8501`.

### Optional: One-click launcher (Windows)

- Double-click `start_app.bat` to auto-start both backend and frontend.

---

## API

- `GET /ping` → returns service status and whether the model loaded.
- `POST /predict` → form-data `file` (image). Returns JSON:

```
{
  "class": "Healthy|Early Blight|Late Blight",
  "confidence": 97.12
}
```

---

## Notes & Tips

- Model path is configured in `api/main.py` as `../training/models/1.keras`.
- If using CPU-only, consider `tensorflow-cpu` instead of `tensorflow`.
- Image file names in `website/images/` should match the code (lowercase `.jpg`).
- On Linux/macOS, case sensitivity matters; keep image names consistent.

---

## Tech Stack

- `Python`, `TensorFlow/Keras`, `NumPy`, `Pillow`
- `FastAPI`, `Uvicorn`
- `Streamlit`

---

## Credits

- Developed by: Abhishek Maheshwari & Team
- Built with: FastAPI + Streamlit

---

## License

This repository is for educational purposes. Add your preferred license if you plan to distribute.






