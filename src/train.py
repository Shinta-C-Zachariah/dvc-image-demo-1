import os
from glob import glob
import joblib

def train_model(image_folder, model_path="models/model.pkl"):
    images = glob(os.path.join(image_folder, "*.jpg"))
    print(f"Training model with {len(images)} images...")

    # Dummy model: just store number of images
    model = {"num_images": len(images)}
    
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model("data/images")

