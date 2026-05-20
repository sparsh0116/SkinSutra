import torch
from model.model_arch import get_model
from config import MODEL_PATH

model = get_model()

model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

print("MODEL LOADED SUCCESSFULLY")