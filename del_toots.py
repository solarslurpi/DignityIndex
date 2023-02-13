import json
from mastodon import Mastodon


OAuth_token = None
try:
    with open('oauth.json', 'r') as file:
        tokens = json.load(file)
        OAuth_token = tokens["sparrow_oauth"]
except Exception as e:
    print(f"Error trying to open oauth.json.  The error is {e}")
    exit(0)
# , debug_requests= True
mastodon = Mastodon(access_token = OAuth_token, api_base_url="https://vintageracing.social" )
# Delete all toots/posts/statuses (whatever you want to call them)
[mastodon.status_delete(toot["id"]) for toot in mastodon.timeline_home()]
print("DONE.")