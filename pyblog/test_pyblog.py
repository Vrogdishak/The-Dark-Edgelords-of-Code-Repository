from pyblog import get_all
from pyblog import get_post_titles
from pyblog import get_post_content
from pyblog import post_post
from pyblog import read_file


def test_get_all():
    result = get_all()
    assert type(result) == list


def test_get_post_titles():
    result = get_post_titles()
    assert type(result) == str


def test_get_post_content():
    result = get_post_content(1)
    assert type(result) == str


def test_post_post():
    result = post_post("test_post_body")
    assert result == 201


def test_read_file():
    result = read_file("test_post_body")
    assert type(result) == tuple


def test_blog_menu():
    pass


def test_parse_arguements():
    pass
