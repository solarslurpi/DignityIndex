import json
from mastodon import Mastodon
from dignityindex_code import DignityIndex

pure_red = "\033[0;31m"
dark_green = "\033[0;32m"
original = '\033[0m'

def main():
    # Log into Mastodon using OAuth.
    # The OAuth key is in our .bashrc file as an env variable.
    #api_key = os.environ.get('API_KEY')
    # mastodon = Mastodon(access_token = f"{api_key}", api_base_url="https://vintageracing.social", debug_requests= True )
    # Load the JSON file
    OAuth_token = None
    try:
        with open('oauth.json', 'r') as file:
            tokens = json.load(file)
            OAuth_token = tokens["sparrow_oauth"]
    except Exception as e:
        print(f"Error trying to open oauth.json.  The error is {e}")
        exit(0)
    mastodon = Mastodon(access_token = OAuth_token, api_base_url="https://vintageracing.social", debug_requests= False )
    # Grab the "Toots" from the home timeline
    toots = mastodon.timeline_home()
    # Assign a Dignity Index
    ## Initialize a DignityIndex class 
    di = DignityIndex()
    ## Set a dignity_threshold to the "worst" text allowed
    dignity_threshold = 5
    for toot in toots:
        dignity_index = di.index(toot['content'])
        if dignity_index < dignity_threshold:
            # Add a content warning...TODO: Whatever is appropriate.....
            mastodon.status_update(toot['id'],spoiler_text='WARNING! THIS TOOT LACKS DIGNITY!',status=toot['content'])



if __name__ == "__main__":
    main()