from ensta import Host
from FollowCheaters import compare_lists  # Import the function from your other file

host = Host("username", "password")

def unfollow_cheaters(username):
    cheaters = compare_lists(username)

    for cheater in cheaters:
        print(f"Unfollowing {cheater}...")
        host.unfollow(cheater)

unfollow_cheaters("fenerbaahce8282")