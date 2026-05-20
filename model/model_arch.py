import torch.nn as nn
from torchvision import models

def get_model():
    model = models.resnet50(pretrained=True)

    for param in model.parameters():
        param.requires_grad = False

    #SAME AS TRAINING
    model.fc = nn.Linear(model.fc.in_features, 7)

    return model