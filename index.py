#!/bin/env python3

from fbchat import Client
from fbchat.models import *

email = "your email here"
password = "your password here"

client = Client(email, password)

images = list(client.fetchThreadImages(thread_id="3388711257902749"))

print(f"Number of images: {len(images)}")

for img in images[:-2]:
    if hasattr(img, "large_preview_url"):
        url = img.large_preview_url
        print(url)
