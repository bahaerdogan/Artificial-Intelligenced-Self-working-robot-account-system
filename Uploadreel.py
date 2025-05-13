from ensta import Host

def upload_reel(video_path, thumbnail_path, caption):
    """
    Uploads a reel with the specified video, thumbnail, and caption.
    
    Parameters:
    video_path (str): The path to the video file.
    thumbnail_path (str): The path to the thumbnail image file.
    caption (str): The caption for the reel.
    """
    try:
        host = Host("username", "password")
        host.upload_reel(video_path=video_path, thumbnail_path=thumbnail_path, caption=caption)
        print("Reel uploaded successfully!")
    except Exception as e:
        print(f"Error uploading reel: {e}")

# # Örnek kullanım:
# upload_reel(video_path="Video.mp4", thumbnail_path="Thumbnail.jpg", caption="Enjoying the winter! ⛄")
