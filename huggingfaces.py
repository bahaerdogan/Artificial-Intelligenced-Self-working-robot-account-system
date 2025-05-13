import schedule
import time
import random
from ensta import Host
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Create Instagram host and profile
host = Host("username", "password")
profile = host.profile("neymarjr")

# Rasgele yorum ve beğeni listeleri
comments = ["Harika bir foto!", "Bu fotoğraf muhteşem!", 
"Çok güzel!","canimmmm", "Mükemmel!", "Bunu seviyorum!", 
"Harika görünüyor!", "Bunu beğendim!"]
emojis = ["👍", "❤️", "😍", "🔥", "💯", "🌟", "🙌", "🎉"]

# Load pre-trained model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_image_caption(image_path):
    image = Image.open(image_path)

    inputs = processor(images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    caption = processor.decode(probs)

    return caption

def post_photo():
    """
    Uploads a photo to Instagram.
    """
    try:
        photo_path = "second.png"  
        upload = host.get_upload_id(photo_path)
        caption = get_image_caption(photo_path) 
        host.upload_photo(upload, caption=caption)
        print("Photo posted successfully!")
    except Exception as e:
        print(f"Error posting photo: {e}")

def update_profile_information(display_name, bio):
    """
    Updates the Instagram profile information.
    """
    try:
        host.change_display_name(display_name)
        host.change_bio(bio)
        print("Profile information updated successfully!")
    except Exception as e:
        print(f"Error updating profile information: {e}")

def schedule_posting():
    """
    Schedules the photo upload process at a random hour.
    """
    try:
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        schedule.every().day.at(f"{random_hour:02d}:{random_minute:02d}").do(post_photo)
        print(f"Photo will be uploaded at {random_hour:02d}:{random_minute:02d}.")
    except Exception as e:
        print(f"Error scheduling posting: {e}")

def add_comment(post_url):
    """
    Adds a comment to the specified post.
    """
    try:
        post_id = host.get_post_id(post_url)
        comment = random.choice(comments) + " " + random.choice(emojis)
        host.comment(comment, post_id)
        print("Comment added successfully!")
    except Exception as e:
        print(f"Error adding comment: {e}")

def follow_unfollow_user(username, action):
    """
    Follows or unfollows the specified user.
    """
    try:
        if action == "follow":
            print(host.follow(username))
        elif action == "unfollow":
            print(host.unfollow(username))
        else:
            print("Invalid action!")
    except Exception as e:
        print(f"Error performing user follow/unfollow: {e}")

if __name__ == "__main__":
    try:
        update_profile_information("Fenerbahce 12.adam", "Adam gibi adam")
        schedule_posting()

        while True:
            schedule.run_pending()
            time.sleep(60)  # Rasgele gecikme ekleme süresi
            # Rasgele yorum ekleme
            add_comment("https://www.instagram.com/p/C55O2XfgbVl/")
            # Rasgele bir kullanıcıyı takip etme veya takibi bırakma
            follow_unfollow_user("leomessi", random.choice(["follow", "unfollow"]))
    except KeyboardInterrupt:
        print("Automation stopped by the user")