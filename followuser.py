# import schedule
# import time
# import random
from ensta import Host

host = Host("username", "password")
profile = host.profile("neymarjr")


def follow_user(username):
    try:
        print(host.follow(username))
    except Exception as e:
        print(f"Error following user: {e}")