import schedule
import time
import random
from ensta import Host

host = Host("fenerbaahce8282", "10suzolmaz")
profile = host.profile("neymarjr")


def unfollow_user(username):
    try:
        print(host.unfollow(username))
    except Exception as e:
        print(f"Error unfollowing user: {e}")