from pyblog import *

def test_get_all():
	result = get_all()
	assert type(result) == list

def test_get_post_titles():
    result = get_post_titles()
    assert type(result) == str

def test_get_post_content():
    result = get_post_content(1)
    assert type(result) == str