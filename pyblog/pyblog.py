#!/usr/bin/env python3
""" TDELoC Pyblog """

import os
import re
import requests
import argparse
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

        # print(data[i]["title"]["rendered"])
        # print(str(i))
    # print(titles)
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
    # print(formatted_post)
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
        user_selection = 0
        user_selection2 = 0
        print("""
        Welcome to the Dark Edgelords of Codes Blog program.
        Please make a selection from our Dark Menu:
        1. Get post Titles
        2. Get contents of a post
        3. Make a new post
        4. Exit program
        """)
        try:
            user_selection = int(input("Enter a number --->  "))
        except ValueError:
            print("You have made an invalid selection, please try again or press cntl^c to end it all.")

        if user_selection == 1:
            titles = get_post_titles()
            print("""
            Here lie the following posts in the domain of THE dark edgelords:
            """)
            print(titles)
        elif user_selection == 2:
            user_selection2 = int(input("Please select a post number: "))
            print(get_post_content(user_selection2))
        elif user_selection == 3:
            file_location = input(
                "Please enter a file name with an absolute path: ")
            post_post(file_location)
        elif user_selection == 4:
            print("""
    May you find your way in the darkness that no one else can understand.""")
            break
        else:
            print("You have made an invalid selection, please try again or press cntl^c to end it all.")


def parse_arguements():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("--menu", help="Launches the blog posting interactive menu")
    parser.add_argument("--latest", help="Gets the latest post", action="store_true")
    parser.add_argument("--post", help="Make a new post from a file", type=str)

    # Read arguments from command line
    args = parser.parse_args()

    if args.menu:
        blog_menu()

    elif args.latest:
        print(get_post_content(0))

    elif args.post:
        post_post(args.post)

    else:
        print("Please use an argument: --menu --latest --post")

    return


parse_arguements()


# get_post_titles()
# get_post_content(0)
# post_post()
# print(read_file("/home/rknepper/edgepost"))
# blog_menu()
# get_latest_post()
