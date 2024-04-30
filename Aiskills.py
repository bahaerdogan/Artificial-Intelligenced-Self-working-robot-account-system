import openai
from ensta import Host
# from postphoto import post_photo
openai.api_key = 'your-chatgpt-key'

def generate_caption():
    """
    Generates a caption using GPT-3.
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a creative caption for an Instagram post:",
        temperature=0.5,
        max_tokens=60
    )
    return response.choices[0].text.strip()

def generate_comment():
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a positive comment for an Instagram post:",
        temperature=0.5,
        max_tokens=30
    )
    return response.choices[0].text.strip()


def post_photo():
    """
    Uploads a photo to Instagram.
    """
    try:
        photo_path = "image.png"  
        upload = host.get_upload_id(photo_path)
        caption = generate_caption()  # Generate caption using GPT-3
        host.upload_photo(upload, caption=caption)
        print("Photo posted successfully!")
    except Exception as e:
        print(f"Error posting photo: {e}")

def add_comment(post_url):
    """
    Adds a comment to the specified post.
    """
    try:
        post_id = host.get_post_id(post_url)
        comment = generate_comment()  # Generate comment using GPT-3
        host.comment(comment, post_id)
        print("Comment added successfully!")
    except Exception as e:
        print(f"Error adding comment: {e}")