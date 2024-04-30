from ensta import Host

def get_profile_info(username, password, target_username):
    """
    Retrieves profile information of a target user.
    
    Parameters:
    username (str): Your Instagram username.
    password (str): Your Instagram password.
    target_username (str): The username of the target user whose profile information to retrieve.
    """
    try:
        host = Host(username, password)
        profile = host.profile(target_username)
        print("Full Name:", profile.full_name)
        print("Biography:", profile.biography)
        print("Follower Count:", profile.follower_count)
    except Exception as e:
        print(f"Error retrieving profile information: {e}")

# # Örnek kullanım:
# get_profile_info("your_username", "your_password", "leomessi")
