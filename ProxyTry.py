from ensta import Host
from ensta import Mobile


host = Host("fenerbaahce8282", "10suzolmaz")
# mobile = Mobile("fenerbaahce8282", "10suzolmaz")
# mobile.change_profile_picture("image.jpg")

posts = host.posts("istegundem", 0)  # Want full list? Set count to '0'

for post in posts:
    print(post.caption_text)
    print(post.like_count)    
