# from ensta import Host

# def like_unlike_post(username, password, post_url):
#     """
#     Likes and then unlikes a specific post.
    
#     Parameters:
#     username (str): Your Instagram username.
#     password (str): Your Instagram password.
#     post_url (str): The URL of the post.
#     """
#     try:
#         host = Host(username, password)
#         post_id = host.get_post_id(post_url)
#         host.like(post_id)
#         print("Post liked!")
#         host.unlike(post_id)
#         print("Post unliked!")
#     except Exception as e:
#         print(f"Error liking/unliking post: {e}")

# # # Örnek kullanım:
#  like_unlike_post("fenerbaahce8282", "10suzolmaz", "https://www.instagram.com/p/C53dvMZooKq/")

from ensta import Host

host = Host("fenerbaahce8282", "10suzolmaz")
post_id = host.get_post_id("https://www.instagram.com/p/Czr2yLmroCQ/")

host.like(post_id)
# host.unlike(post_id)
