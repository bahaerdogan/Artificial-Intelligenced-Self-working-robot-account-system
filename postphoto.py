# import schedule
# import time
# import random
# from ensta import Host

# host = Host("fenerbaahce8282", "10suzolmaz")"
# profile = host.profile("neymarjr")

# def post_photo():
#     try:
#         photo_path = "second.png"  # Example path
#         upload = host.get_upload_id(photo_path)
#         caption = "Your caption here"  # Example caption
#         host.upload_photo(upload, caption=caption)
#         print("Photo posted successfully!")
#     except Exception as e:
#         print(f"Error posting photo: {e}")

import schedule
import time
import random
from ensta import Host
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

host = Host("fenerbaahce8282", "10suzolmaz")
profile = host.profile("neymarjr")

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32<")

def get_image_caption(image_path):
    image = Image.open(image_path)

    inputs = processor(images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    caption = processor.decode(probs)

    return caption

def post_photo():
   
    try:
        photo_path = "second.png"  
        upload = host.get_upload_id(photo_path)
        caption = get_image_caption(photo_path) 
        host.upload_photo(upload, caption=caption)
        print("Photo posted successfully!")
    except Exception as e:
        print(f"Error posting photo: {e}")

if __name__ == "__main__":
    try:
        post_photo()
    except KeyboardInterrupt:
        print("Automation stopped by the user")