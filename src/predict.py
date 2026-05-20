import torch
from model.model_arch import get_model
from config import MODEL_PATH
from src.preprocess import preprocess_image

device = "cuda" if torch.cuda.is_available() else "cpu"

model = get_model()
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# CORRECT ORDER
class_names = [
    "Actinic Keratosis",
    "Basal Cell Carcinoma",
    "Benign Keratosis",
    "Dermatofibroma",
    "Melanoma",
    "Nevus",
    "Vascular Lesion"
]

def predict(image):
    image = preprocess_image(image).to(device)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)

        top3_prob, top3_idx = torch.topk(probs, 3)

    results = []
    for i in range(3):
        results.append((
            class_names[top3_idx[0][i]],
            float(top3_prob[0][i])
        ))

    return results