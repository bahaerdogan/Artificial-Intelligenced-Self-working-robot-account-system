# import schedule
# import time
# import random
# from ensta import Host

# host = Host("fenerbaahce8282", "10suzolmaz")
# profile = host.profile("neymarjr")

# def schedule_posting():
#     try:
#         random_hour = random.randint(0, 23)
#         schedule.every().day.at(f"{random_hour}:00").do(post_photo)
#         print(f"Photo will be posted at {random_hour}:00")
#     except Exception as e:
#         print(f"Error scheduling posting: {e}")

# if __name__ == "__main__":
#     try:
#         host.change_display_name("Fenerbahce 12.adam")
#         host.change_bio("Adam gibi adam")

#         schedule_posting()

#         while True:
#             schedule.run_pending()
#             time.sleep(60)
#     except KeyboardInterrupt:
#         print("Automation stopped by user")
import schedule
import time
import random
from ensta import Host
from Cheataction import unfollow_cheaters  # Import the function

host = Host("fenerbaahce8282", "10suzolmaz")
profile = host.profile("neymarjr")

def schedule_posting():
    try:
        random_hour = random.randint(0, 23)
        schedule.every().day.at(f"{random_hour}:00").do(post_photo)
        print(f"Photo will be posted at {random_hour}:00")
    except Exception as e:
        print(f"Error scheduling posting: {e}")

def schedule_unfollowing():
    try:
        for _ in range(2):  # Schedule two unfollowings per day
            random_hour = random.randint(0, 23)
            random_minute = random.randint(0, 59)
            schedule.every().day.at(f"{random_hour}:{random_minute}").do(unfollow_cheaters, 'leomessi')
            print(f"Will unfollow cheaters at {random_hour}:{random_minute}")
    except Exception as e:
        print(f"Error scheduling unfollowing: {e}")

if __name__ == "__main__":
    try:
        host.change_display_name("Fenerbahce 12.adam")
        host.change_bio("Adam gibi adam")

        schedule_posting()
        schedule_unfollowing()  # Schedule the unfollowing

        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Automation stopped by user")