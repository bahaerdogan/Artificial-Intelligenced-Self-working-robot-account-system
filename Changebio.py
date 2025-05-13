from ensta import Host

def change_bio(new_bio):
    """
    Changes the bio of the host.
    
    Parameters:
    new_bio (str): The new bio text to set.
    """
    try:
        host = Host("username", "password")
        host.change_bio(new_bio)
        print("Bio changed successfully!")
    except Exception as e:
        print(f"Error changing bio: {e}")

# # Örnek kullanım:
change_bio("Ath")
