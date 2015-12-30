import random

import flickrapi

from settings_loader import config

def find_picture(topic, potential_keywords):
    flickr = flickrapi.FlickrAPI(config["API_KEY"], config["API_SECRET"], format='parsed-json')
    pictures = flickr.photos.search(tags=topic, text=random.choice(potential_keywords),
                                    licenses=[2, # cc-by-nc 
                                              4, # cc-by
                                              7],# no known copyright restrictions
                                    per_page=10) 
    print(pictures)
    pic = random.choice(pictures['photos']['photo']) 
    pic_url = "https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg".format(**{'farm-id': pic['farm'],
                                                                                               'server-id': pic['server'],
                                                                                               'id': pic['id'],
                                                                                               'secret': pic['secret']})
    print pic_url


for _ in range(1, 5):
    find_picture("dog", ["curious", "nighttime"])




