import requests
import json
import sys
import os
import argparse
import re
from datetime import datetime
from requests.auth import HTTPBasicAuth

# Read In Env Variables

wp_user = os.environ.get('wp_admin')
wp_pass = os.environ.get('wp_pass')
wp_url = os.environ.get('wp_url')

# Get current date and time for new posts
current_date = datetime.now()
blog_post_date = current_date.strftime('%Y-%m-%dT%H:%M:%M')

# Create authentication portion of request
basic = HTTPBasicAuth(wp_user, wp_pass)

# Wordpress API header
headers = {
  'Accept': 'application/json',
  }

# Use argparse to take in variables
my_parser = argparse.ArgumentParser(
    prog='pyblog',
    description='Program used to read and make blog posts'
    )
my_parser.add_argument('command', type=str)
my_parser.add_argument(
    '-f',
    '--file',
    help="Name of the file to create blog post from"
    )
my_parser.add_argument(
    'text_input',
    nargs='?',
    type=str,
    default="-",
    help="Name of the file to create blog post from"
    )

# Set args to variables taken in by argparse
args = my_parser.parse_args()


def post():

    title = "Need to define how to get this from stdin"
    excerpt = "Same as title"

    rest_method = "POST"
    url = wp_url
    payload = {'Content': 'Test Content',
               'title': title,
               'excerpt': excerpt,
               'date': blog_post_date,
               'status': 'publish'
               }

    response = requests.request(
        rest_method,
        url,
        auth=basic,
        headers=headers,
        data=payload
        )

    pyblog_request_data = response.json()

    # print(response.text)
    print(json.dumps(pyblog_request_data, indent=4, sort_keys=True))


def upload():
    input_file = args.file or args.text_input
    if input_file == "-":
        file = sys.stdin
    else:
        file = open(input_file)

    lines = file.read()
    title = lines.split('\n', 1)[0]
    excerpt = lines.split('\n', 2)[2]

    file.close()

    rest_method = "POST"
    url = wp_url
    payload = {'Content': 'File Content',
               'title': title,
               'excerpt': excerpt,
               'date': blog_post_date,
               'status': 'publish',
               }

    response = requests.request(
        rest_method, url,
        auth=basic,
        headers=headers,
        data=payload
        )

    pyblog_request_data = response.json()

    pyblog_request_data = response.json()

    date_response = pyblog_request_data["date"]
    title_response = pyblog_request_data["title"]["rendered"]
    excerpt_response = pyblog_request_data["excerpt"]["rendered"]
    excerpt_response = re.sub(r'<.*?>', '', excerpt_response)

    print(f' Date:  {date_response} \n\n Title: {title_response} \
        \n\n Excerpt: {excerpt_response}')


def read():

    rest_method = "GET"
    url = wp_url + "?per_page=1"

    response = requests.request(rest_method, url, headers=headers)

    pyblog_request_data = response.json()

    title_response = pyblog_request_data[0]["title"]["rendered"]
    excerpt_response = pyblog_request_data[0]["excerpt"]["rendered"]
    excerpt_response = re.sub(r'<.*?>', '', excerpt_response)

    print(f' Title: {title_response} \n\n Excerpt: {excerpt_response}')


if args.command == "read":
    read()

if args.command == "upload":
    upload()