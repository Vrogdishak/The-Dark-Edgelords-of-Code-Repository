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

def test_read_file():
    result = read_file("/home/rknepper/edgepost")
    assert type(result) == str