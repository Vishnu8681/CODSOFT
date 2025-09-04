import warnings
warnings.filterwarnings("ignore")

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"   

from transformers import logging
logging.set_verbosity_error()  
import warnings
warnings.filterwarnings("ignore")

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  

import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_caption(image_path):
    image = Image.open(image_path)
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values.to(device)
    
    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return caption

if __name__ == "__main__":
    test_image = "Aeroplane.jpg"  
    print("Caption:", generate_caption(test_image))
