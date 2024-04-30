from ensta import Host

def get_followings_list(username, count=100):
    """
    Retrieves a list of followings for the specified username.
    
    Parameters:
    username (str): The username of the account whose followings to retrieve.
    count (int): The number of followings to retrieve. Set to 0 to retrieve all followings.
    """
    try:
        host = Host("fenerbaahce8282", "10suzolmaz")
        followings = host.followings(username, count=count)
        for user in followings:
            print(user.username)
    except Exception as e:
        print(f"Error getting followings list: {e}")

# # Örnek kullanım:
# get_followings_list("neymarjr")
