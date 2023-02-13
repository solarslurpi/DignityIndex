import os
import requests
import re
from typing import List, Tuple
from mastodon import Mastodon


class DignityIndex:
    
    def __init__(self):
        """Initialize variables needed for access to
        the Mastodon posts as well as set up the dignity
        threshold. 

        """
        # Load the API key from the environment.  We use OAuth to login.
        self.api_key = os.environ.get('API_KEY')



    
    def index(self, text: str) -> int:
        """Return the Dignity Index for the text

        Args:
            text (str): String of text to apply a Dignity Index to

        Returns:
            int: The Dignity Index for the text.
        """
        # TODO: DIGNITY INDEX ALGORITHM
        # THIS IS DUMMY CODE...Very simple...just for illustration
        # Really simple word match -> dignity_index
        # if text contains:
        #   evil      -> di = 2
        #   destroy   -> di = 1
        #   bad       -> di = 3
        #   different -> di = 4
        di = {"destroy"   : 1,
              "evil"      : 2,
              "bad"       : 3,
              "different" : 4  }
        unacceptable_words = {"destroy", "evil",  "bad", "different"}
        # re.findall returns a list of the words found.
        match = re.findall(f"\\b({'|'.join(unacceptable_words)})\\b", text, re.IGNORECASE)
        if match:
            unacceptable_word = match[0].lower()
            dignity_index = di[unacceptable_word]
            return dignity_index
        else:
            # This is a dumb proof of concept.  I'm showing action on a negative toot.
            # Clearly the algorithm will address all numbers.
            return 6
        ######################

    def flag_post(self,post_id) -> int:
        header = {
            "Authorization":  f"Bearer {self.api_key}",
             "Content-Type": "application/json"
        }

        data = {
            "text": "Hello world",
            "sensitive": True
        }
        url = "https://vintageracing.social/api/v1/statuses/" + post_id

        try:
            response = requests.put(url, headers=header, json=data)
            response.raise_for_status()   # Raise HTTP error if response.status_code did not return 200
            return True
        except requests.HTTPError as e:
            raise ValueError(f"ERROR: {e} Invalid status code: {response.status_code}")  

    def unacceptable_posts(self) -> List[Tuple[str, int]]:
        """
        Returns a list of tuples, where each tuple consists of the text of a post and its corresponding dignity index.

        Raises:
            ValueError: If the request for the posts fails due to an HTTP error.

        Returns:
            List[Tuple[str, int]]: A list of tuples, where each tuple is of the format (post text, dignity index).
        """
        try:
            header = {
                "Authorization": f"Bearer {self.api_key}"
            }
            response = requests.get('https://vintageracing.social/api/v1/timelines/home', headers=header)
            # 200 = OK. The request was handled successfully.
            # 4xx = Client error. Your request was not correct. Most commonly, you may see 
            # 401 Unauthorized, 404 Not Found, 410 Gone, or 422 Unprocessed.
            # 5xx = Server error. Something went wrong while handling the request. Most commonly, 
            # you may see 503 Unavailable.
            response.raise_for_status()   # Raise HTTP error if response.status_code did not return 200
            # Get the posts.
            posts = response.json()
        except requests.HTTPError as e:
            raise ValueError(f"ERROR: {e} Invalid status code: {response.status_code}")

        # Flag unacceptable posts
        for post in posts:
            dignity_index_of_post = self.index(post["content"])
            if (dignity_index_of_post and dignity_index_of_post < self.dignity_threshold):
                self.flag_post(post['id'])

        # Return the list of posts and their dignity index.

        # return [(post["content"], self.index(post["content"])) for post in posts if self.index(post["content"]) < self.dignity_threshold]
        return

    def about(self):
        # TODO: return text defining salient parts about the dignity index
        pass
