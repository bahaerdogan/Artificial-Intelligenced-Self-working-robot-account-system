import schedule
import time
import random
from ensta import Host

host = Host("username", "password")
profile = host.profile("neymarjr")

def get_private():
    try:
        print(host.switch_to_private_account())
    except Exception as e:
        print(f"Error switching to private account: {e}")