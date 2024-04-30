import time
import schedule
from addcomment import add_comment
from Changebio import change_bio
from Changename import change_display_name
from Cheataction import unfollow_cheaters
from compare_lists import compare_lists
from Followingslist import get_followings_list
from Followerslist import get_followers
from Getinformation import get_profile_info
from Unfollowuser import unfollow_user
from postphoto import post_photo
# from schedule_posting import schedule_posting
# from update_profile_information import update_profile_information
# from schedule_comments_and_follows import schedule_comments_and_follows

def main():
    try:
        update_profile_information.update("Fenerbahce 12.adam", "Adam gibi adam")
        schedule_posting.schedule()
        schedule_comments_and_follows.schedule()

        while True:
            schedule.run_pending()
            time.sleep(60)  # Rasgele gecikme ekleme süresi
    except KeyboardInterrupt:
        print("Automation stopped by the user")

if __name__ == "__main__":
    main()