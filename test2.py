from mastodon import Mastodon

# Log into Mastodon with OAuth.

mastodon = Mastodon(access_token = "pPeDjaqPoQqcv351X_SWpGsXaxpUIxmRZZlfcFjh4pk", api_base_url="https://vintageracing.social" )
# retrieve the Toot with id 109775025752422897

# get the latest toots from the public timeline
toots = mastodon.timeline_home()

# loop through the toots
for toot in toots:
    # access information about each toot, such as the toot's content, creation time, etc.
    print(toot["content"])
    print(toot["created_at"])
    print("---")