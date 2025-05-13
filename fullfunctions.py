import schedule
import time
import random
import os
from ensta import Host
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Instagram credentials from environment variables
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
    raise ValueError("Instagram credentials not found in environment variables. Please set INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD in .env file")

# Create Instagram host
host = Host(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

# Comments and emojis for random selection
comments = [
    "Harika bir foto!",
    "Bu fotoğraf muhteşem!",
    "Çok güzel!",
    "Mükemmel!",
    "Bunu seviyorum!",
    "Harika görünüyor!",
    "Bunu beğendim!"
]

emojis = ["👍", "❤️", "😍", "🔥", "💯", "🌟", "🙌", "🎉"]

def post_photo(photo_path=None, caption=None):
    """
    Uploads a photo to Instagram.
    
    Args:
        photo_path (str): Path to the photo file. If None, will use default from env.
        caption (str): Caption for the photo. If None, will use default from env.
    """
    try:
        if not photo_path:
            photo_path = os.getenv('DEFAULT_PHOTO_PATH')
            if not photo_path:
                raise ValueError("No photo path provided and DEFAULT_PHOTO_PATH not set in environment variables")
        
        if not os.path.exists(photo_path):
            raise FileNotFoundError(f"Photo file not found at {photo_path}")
            
        if not caption:
            caption = os.getenv('DEFAULT_CAPTION', '')
            
        upload = host.get_upload_id(photo_path)
        host.upload_photo(upload, caption=caption)
        print("Photo posted successfully!")
    except Exception as e:
        print(f"Error posting photo: {e}")
        raise

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

def list_followers_followings(username, followers=True):
    """
    Lists followers or followings of the specified user.
    """
    try:
        if followers:
            users = host.followers(username, count=100)  # Set count to '0' to get the full list
            print("Followers:")
        else:
            users = host.followings(username, count=100)  # Set count to '0' to get the full list
            print("Followings:")
        
        for user in users:
            print(user.username)
    except Exception as e:
        if followers:
            print(f"Error listing followers: {e}")
        else:
            print(f"Error listing followings: {e}")

def switch_account_privacy(public=True):
    """
    Changes the account privacy settings.
    """
    try:
        if public:
            print(host.switch_to_public_account())
            print("Account is now public.")
        else:
            print(host.switch_to_private_account())
            print("Account is now private.")
    except Exception as e:
        print(f"Error changing account privacy settings: {e}")

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

if __name__ == "__main__":
    try:
        # Example usage - replace with your desired actions
        schedule_posting()

        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Automation stopped by the user")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
