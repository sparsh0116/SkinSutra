import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "HAM10000_model (1).pth")

DEVICE = "cpu"
IMAGE_SIZE = 224