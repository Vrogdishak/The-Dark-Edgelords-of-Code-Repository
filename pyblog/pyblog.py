import requests
import json
import html

def get_all():
    response = requests.get("http://ec2-44-202-229-125.compute-1.amazonaws.com:8088/wp-json/wp/v2/posts")
    data = response.json()
    return data

def get_post_titles():
    titles = ""
    data = get_all()
    for i in range(len(data)):
        titles += str(i) + ". " + data[i]["title"]["rendered"] + "\n"
        print(str(i))
    return titles

def get_post_content(post_number):
    data = get_all()
    title = data[post_number]["title"]["rendered"]
    body = data[post_number]["content"]["rendered"]    
    content = data[post_number]["content"]["rendered"]
    content = html.unescape(content)
    date = data[post_number]["date"]
    formatted_post = title + "    " + date + "\n" + content
    print(content)
    return content

get_post_content(1)

