import os
import logging
import sys
import pusher

from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("PUSHER_APP_ID")
KEY = os.getenv("PUSHER_KEY")
SECRET = os.getenv("PUSHER_SECRET")
CLUSTER = os.getenv("PUSHER_CLUSTER")


class Subscription:
    def __init__(self):
        self.pusher = pusher.Pusher(
            app_id=APP_ID, key=KEY, secret=SECRET, cluster=CLUSTER,
        )

    def send(self, data):
        self.pusher.trigger("flimmer", "beacon", data)


subscription = Subscription()
