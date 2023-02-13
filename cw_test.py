import os
from mastodon import Mastodon

pure_red = "\033[0;31m"

## Log in using OAuth.
api_key = os.environ.get('API_KEY')
mastodon = Mastodon(access_token = f"{api_key}", api_base_url="https://vintageracing.social", debug_requests= True )
## Get a Toot
a_toot = mastodon.timeline_public()
# Get the ID of the toot you want to modify
toot_id = a_toot[0]['id']
# Set the content warning for the toot
mastodon.status_update(
    toot_id,
    status= a_toot[0]['content'],
    spoiler_text=pure_red + 'CW: This toot contains graphic content' 
)