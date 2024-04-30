from ensta import Host

def change_display_name(new_name):
    """
    Changes the display name of the host.
    
    Parameters:
    new_name (str): The new display name to set.
    """
    try:
        host = Host("fenerbaahce8282", "10suzolmaz")
        host.change_display_name(new_name)
        print("Display name changed successfully!")
    except Exception as e:
        print(f"Error changing display name: {e}")

# # Örnek kullanım:
# change_display_name("Bahae")
