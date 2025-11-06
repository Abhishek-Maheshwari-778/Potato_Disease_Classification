from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

# Allow CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "*",  # Allow all origins for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define class names
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Load the model
model_path = "../training/models/1.keras"

# Check if model exists
if not os.path.exists(model_path):
    print(f"Model not found at {model_path}. Please check the path.")
    model = None
else:
    try:
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    # Resize image to match the input size expected by the model
    image = image.resize((256, 256))
    image = np.array(image)
    return image


@app.get("/")
async def root():
    return {"message": "Welcome to Potato Disease Classification API"}


@app.get("/ping")
async def ping():
    return {"status": "active", "model_loaded": model is not None}


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    if model is None:
        return {"error": "Model not loaded. Please check server logs."}
    
    image = read_file_as_image(await file.read())
    
    # Add batch dimension and ensure image is in the right format
    img_batch = np.expand_dims(image, 0)
    
    # Make prediction
    predictions = model.predict(img_batch)
    
    # Get predicted class and confidence
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]) * 100)
    
    return {
        "class": predicted_class,
        "confidence": confidence
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)