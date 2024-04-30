from ensta import Guest

def check_username_availability(username):
    """
    Checks the availability of a username.
    
    Parameters:
    username (str): The username to check.
    
    Returns:
    bool: True if the username is available, False otherwise.
    """
    try:
        guest = Guest()
        return guest.username_availability(username)
    except Exception as e:
        print(f"Error checking username availability: {e}")
        return False

# # Örnek kullanım:
# print(check_username_availability("theusernameiwant"))
