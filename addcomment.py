import schedule
import time
import random
from ensta import Host

host = Host("fenerbaahce8282", "10suzolmaz")

def add_comment(post_url, comment):
    """
    Adds a comment to the specified post.
    """
    try:
        post_id = host.get_post_id(post_url)
        host.comment(comment, post_id)
        print("Comment added successfully!")
    except Exception as e:
        print(f"Error adding comment: {e}")