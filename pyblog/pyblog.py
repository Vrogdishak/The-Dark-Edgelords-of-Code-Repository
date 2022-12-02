#!/usr/bin/env python3
"""
find the sun
"""
import os
import requests

# WORDPRESS_USERNAME = os.environ["WORDPRESS_USERNAME"]
# WORDPRESS_PASSWORD = os.environ["WORDPRESS_PASSWORD"]
# WORDPRESS_URL = os.environ["WORDPRESS_URL"]
WORDPRESS_URL = "http://ec2-44-202-229-125.compute-1.amazonaws.com:8088/wp-json"

# MENU
# - List All Post Titles
# - Retreive A Post
# - Make a Post
# - Exit

def getPostTitles():
    response = requests.get(WORDPRESS_URL+"/wp/v2/posts")
    data = response.json()
    
    for i in range(len(data)):
        title = data[i]["title"]["rendered"]
        print(str(i) + ": " + title)

def getSinglePost(postID):
    response = requests.get(WORDPRESS_URL+"/wp/v2/posts/"+postID)
    data = response.json()

# data = response.json()

# title = data["title"]["rendered"]
# content = data["content"]["rendered"]
# date = data["date"]

# print(f"Blog Post Title: \n " + "-" * 10 + "\n" + title + "\n")
# print(f"Blog Post Content: \n " + "-" * 10 + "\n" + content)
# print(f"Blog Post Date: \n " + "-" * 10 + "\n" + date)

getPostTitles()