#!/usr/bin/env python3
"""
find the sun
"""
import os
import requests

# WORDPRESS_USERNAME = os.environ["WORDPRESS_USERNAME"]
# WORDPRESS_PASSWORD = os.environ["WORDPRESS_PASSWORD"]
# WORDPRESS_URL = os.environ["WORDPRESS_URL"]


def getPostTitles():
    response = requests.get("http://ec2-44-202-229-125.compute-1.amazonaws.com:8088/wp-json/wp/v2/posts")


def getSinglePost():
    pass

response = requests.get("http://ec2-44-202-229-125.compute-1.amazonaws.com:8088/wp-json/wp/v2/posts/1")

data = response.json()

title = data["title"]["rendered"]
content = data["content"]["rendered"]
date = data["date"]

print(f"Blog Post Title: \n " + "-" * 10 + "\n" + title + "\n")
print(f"Blog Post Content: \n " + "-" * 10 + "\n" + content)
print(f"Blog Post Date: \n " + "-" * 10 + "\n" + date)