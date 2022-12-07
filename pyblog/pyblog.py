#!/usr/bin/env python3
""" TDELoC Pyblog """

import os
import re
import requests
from requests.auth import HTTPBasicAuth

WORDPRESS_USER = os.environ["WORDPRESS_USER"]
WORDPRESS_PASSWORD = os.environ["WORDPRESS_PASSWORD"]
WORDPRESS_URL = os.environ["WORDPRESS_URL"]

def get_all():
    """ Retreive All Posts """
    response = requests.get(WORDPRESS_URL+"wp-json/wp/v2/posts", timeout=5)
    data = response.json()
    return data

def get_post_titles():
    """ Retreive Post Titles """
    titles = ""
    data = get_all()
    for i in range(len(data)):
        titles += str(i) + ". " + data[i]["title"]["rendered"] + "\n"
        print(str(i))
    return titles

def get_post_content(post_number):
    """ Retrieve Post Content """
    data = get_all()
    title = data[post_number]["title"]["rendered"]
    content = data[post_number]["content"]["rendered"]
    # RegEx to Strip HTML Tags
    body = re.sub("<[^>]*>", "", content)
    date = data[post_number]["date"]
    formatted_post = title + "    " + date + "\n" + body
    print(formatted_post)
    return formatted_post

def post_post():
    """ Post a Post """
    basic = HTTPBasicAuth(WORDPRESS_USER, WORDPRESS_PASSWORD)
    payload = {
        "title": "this is a title here NEW",
        "content": "I am a Paragraph",
        "status": "publish"
    }
    post = requests.post(
        WORDPRESS_URL+"wp-json/wp/v2/posts",
        auth=basic,
        params=payload,
        timeout=5
    )
    print(WORDPRESS_USER)
    print(post.status_code)

def read_file(filename):
    try:
        file_contents = open(filename, "r")
        contents_storage = file_contents.read()
        file_contents.close()
    except FileNotFoundError:
        print("File not found, please enter a valid file name.")
        return
    return contents_storage

#get_post_content(0)
#post_post()
print(read_file("/home/rknepper/edgepost"))