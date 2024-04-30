from ensta import Host

def get_post_likers(username, password, post_url):
    """
    Retrieves the list of users who liked a specific post.
    
    Parameters:
    username (str): Your Instagram username.
    password (str): Your Instagram password.
    post_url (str): The URL of the post.
    """
    try:
        host = Host(username, password)
        post_id = host.get_post_id(post_url)
        likers = host.likers(post_id)
        for user in likers.users:
            print("Username:", user.username)
            print("Profile Picture URL:", user.profile_picture_url)
    except Exception as e:
        print(f"Error retrieving post likers: {e}")

# # Örnek kullanım:
# get_post_likers("your_username", "your_password", "https://www.instagram.com/p/Czr2yLmroCQ/")
