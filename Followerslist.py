import schedule
import time
import random
from ensta import Host

def get_followers(username, count=100):
    """
    Retrieves a list of followers for the specified username.
    
    Parameters:
    username (str): The username of the account whose followers to retrieve.
    count (int): The number of followers to retrieve. Set to 0 to retrieve all followers.
    
    Returns:
    list: A list of followers.
    """
    try:
        host = Host("fenerbaahce8282", "10suzolmaz")
        followers = host.followers(username, count=count)
        return followers
    except Exception as e:
        print(f"Error retrieving followers: {e}")
        return []

# # Örnek kullanım:
# followers = get_followers("akademisa_", count=100)
# for user in followers:
#     print(user.username)


