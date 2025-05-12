# Self-Working Instagram Automation System

This project is an intelligent automation system for managing Instagram accounts in a human-like manner. It is designed to simulate natural user activity—such as posting, liking, following/unfollowing, editing profile information, and toggling privacy settings—to reduce the risk of detection as a bot.

## Features

* Automatically uploads photos at randomized times
* Follows or unfollows users based on certain conditions (e.g., unfollowing non-followers)
* Leaves random comments and likes on selected profiles
* Updates bio and display name periodically
* Randomly switches account between public and private
* Fully script-based, customizable behavior
* Uses the `ensta` library to interact with Instagram
* Task scheduling via the `schedule` module

## Requirements

* Python 3.8 or above
* Required packages:

```
pip install ensta schedule
```

> Note: If `ensta` is a private or custom library, make sure it's properly included or documented for installation.

## Usage

1. Clone the repository:

```
git clone https://github.com/bahaerdogan/Self-working-robot-account-system.git
cd Self-working-robot-account-system
```

2. Open the main script (e.g., `automation.py`) and replace login credentials and target usernames:

```python
from ensta import Host

host = Host("your_username", "your_password")
profile = host.profile("target_account")
```

3. Run the script:

```
python automation.py
```

The automation will perform actions periodically, including photo uploads, profile edits, following/unfollowing, and posting comments.

## Example Behavior

* Uploads a photo with a preset caption at a random time each day
* Comments on a random post using a selected message and emoji
* Follows and unfollows users randomly to simulate engagement
* Switches privacy settings at intervals
* Updates profile display name and bio occasionally

## Functions Overview

| Function                       | Description                                |
| ------------------------------ | ------------------------------------------ |
| `post_photo()`                 | Uploads a photo with a caption             |
| `follow_unfollow_user()`       | Follows or unfollows a specified user      |
| `add_comment(post_url)`        | Posts a randomized comment on a given post |
| `switch_account_privacy()`     | Toggles the account between public/private |
| `update_profile_information()` | Edits display name and biography           |
| `schedule_posting()`           | Schedules photo uploads at random times    |

## Disclaimer

This project is intended for educational and research purposes only. Use of automated actions on Instagram may violate their terms of service and result in account restrictions. Use at your own risk.

## License

This project is licensed under the MIT License.
