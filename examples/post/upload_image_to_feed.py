import os

from instauto.api.client import ApiClient
from instauto.api import structs as st
from instauto.api.actions import post as ps

if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(user_name=os.environ.get("INSTAUTO_USER") or "your_username", password=os.environ.get("INSTAUTO_PASS") or "your_password")
        client.login()
        client.save_to_disk('./.instauto.save')

    post = ps.PostFeed(
        path='./test_feed.jpg',
        caption='This is an example. Follow me!'
    )
    resp = client.post_post(post, 80)
    print("Success: ", resp.ok)
