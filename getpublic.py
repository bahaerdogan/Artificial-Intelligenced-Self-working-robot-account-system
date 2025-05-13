import schedule
import time
import random
from ensta import Host

host = Host("username", "password")
profile = host.profile("neymarjr")

def get_public():
    try:
        print(host.switch_to_public_account())
    except Exception as e:
        print(f"Error switching to public account: {e}")