from ensta import Host

host = Host("username", "password")

def get_followers_list(username):
    try:
        followers = host.followers(username, count=0)  # Get full list
        return [user.username for user in followers]
    except Exception as e:
        print(f"Error getting followers list: {e}")
        return []

def get_followings_list(username):
    try:
        followings = host.followings(username, count=0)  # Get full list
        return [user.username for user in followings]
    except Exception as e:
        print(f"Error getting followings list: {e}")
        return []

def compare_lists(username):
    followers = set(get_followers_list(username))
    followings = set(get_followings_list(username))

    not_following_back = followings - followers

    return list(not_following_back)  # Return the list instead of printing it *****

    # print(f"People who are not following back: {not_following_back}")

# compare_lists(''akademisa_'')