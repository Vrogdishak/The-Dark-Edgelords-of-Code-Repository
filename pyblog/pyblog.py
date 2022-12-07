#!/usr/bin/env python3
""" TDELoC Pyblog """

import os
import re
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

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
        titles = titles + str(i) + ". " + data[i]["title"]["rendered"] + "\n"
        #print(titles)
        #print(data[i]["title"]["rendered"])
        #print(str(i))
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

def post_post(file_location):
    """ Post a Post """
    date = datetime.now()
    basic = HTTPBasicAuth(WORDPRESS_USER, WORDPRESS_PASSWORD)
    content = read_file(file_location)
    payload = {
        "title": content[1],
        "content": content[0],
        "date": date,
        "status": "publish"
    }
    post = requests.post(
        WORDPRESS_URL+"wp-json/wp/v2/posts",
        auth=basic,
        params=payload,
        timeout=5
    )
    print(WORDPRESS_USER)
    
    return post.status_code

def read_file(filename):
    try:
        file_contents = open(filename, "r")
        title = file_contents.readline().strip("\n")
        contents_storage = file_contents.read()
        file_contents.close()
    except FileNotFoundError:
        print("File not found, please enter a valid file name.")
        return
    return contents_storage, title


def blog_menu():

    while True: 
        print("""
        Welcome to the Dark Edgelords of Codes Blog program. 
        Please make a selection from our Dark Menu:
        1. Get post Titles
        2. Get contents of a post
        3. Make a new post
        4. Exit program
        """)
        user_selection = input("Enter a number --->  ")

        if user_selection == "1": 
            print(get_post_titles())
        elif user_selection == "2":
            user_selection2 = int(input("Please select a post number: "))
            get_post_content(user_selection2)
        elif user_selection == "3":
            file_location = input("Please enter a file name with an absolute path: ")
            post_post(file_location)
        elif user_selection == "4":
            print("May you find your way through the darkness that no one else can understand.")
            break       

#get_post_titles()
#get_post_content(0)
#post_post()
#print(read_file("/home/rknepper/edgepost"))
blog_menu()