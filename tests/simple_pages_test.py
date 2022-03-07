"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<li><a href="/page/about">About</a></li>' in response.data
    assert b'<li><a href="/page/welcome">Welcome</a></li>' in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/page/about")
    assert response.status_code == 200
    assert b"About Page" in response.data


def test_request_welcome(client):
    """This makes the index page"""
    response = client.get("/page/welcome")
    assert response.status_code == 200
    assert b"Welcome Page" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page/page5")
    assert response.status_code == 404
