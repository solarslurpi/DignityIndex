import json
from mastodon import Mastodon



def main():
    # Log into Mastodon using OAuth.
    # The OAuth key is in our .bashrc file as an env variable.
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
    toots_list = [toot.strip() for toot in open("toots_list.txt").readlines()]
    for toot in toots_list:
        input("Press any key to continue...")
        mastodon.status_post(toot, visibility="public")



if __name__ == "__main__":
    main()
