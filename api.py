from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = FastAPI()
model = load_model("MobileNet_RGB-2506.h5")
class_names = ['donut', 'su kem', 'sừng bò', 'tart trứng']

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    pred_index = np.argmax(prediction)
    pred_class = class_names[pred_index]
    confidence = float(np.max(prediction)) * 100

    return {
        "prediction": pred_class,
        "confidence": f"{confidence:.2f}%"
    }
