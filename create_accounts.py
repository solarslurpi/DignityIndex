import os
from mastodon import Mastodon

api_key = os.environ.get('API_KEY')
mastodon = Mastodon(client_id = "ZduHRCo5832kiSGQIwJBp3DGvAWXgk4_IUZtywWpGXw",
                    client_secret = "vjfZ4d35swrrav9fw6WXL3fVnGwrBzXrLwb6JoBK-q8",
                    access_token = f"{api_key}", 
                    api_base_url="https://vintageracing.social"
                    )
account_params = [
                    {"username": "john", "email": "john@example.com", "password": "chance", "agreement": True},
                    {"username": "jane", "email": "john@example.com", "password": "chance", "agreement": True},
                    {"username": "alec", "email": "john@example.com", "password": "chance", "agreement": True},
                ]

for params in account_params:
    mastodon.create_account(**params, return_detailed_error= True)