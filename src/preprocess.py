import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def preprocess_image(image):
    image = image.convert("RGB")
    image = transform(image).unsqueeze(0)
    return image