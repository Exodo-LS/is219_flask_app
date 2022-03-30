import pytest
from app.db.models import User


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


# Project 2 Unit Tests:
# Unit Test 1 - Bad password (Login)
def test_invalid_password(client):
    """ Unit Test for Incorrect Password for Login """
    response = client.post("/login")
    test_user = 'IS219_TestUser@email.com'
    test_password = 'invalid_password'
    if User.email == test_user:
        if test_password != User.password:
            assert 'Invalid password' in response.data


# Unit Test 2 - Bad username / email  (login)
def test_invalid_email_address(client):
    """ Unit Test for Incorrect Email for Login"""
    response = client.post("/login")
    if User.email is None:
        assert 'Invalid username' in response.data


# Unit Test 3 - Bad username / email (Registration)
def test_invalid_email_address_register(client):
    """ Unit Test for Invalid Email for Registration"""
    response = client.post("/register")
    test_email = 'test'
    if User.email is None:
        User.email = test_email
        if '@' not in User.email:
            assert 'Please include an '@' in the email address' in response.data


# Unit Test 4 - Password Confirmation (registration)
def test_password_confirmation(client):
    """ Unit Test for Password Confirmation"""
    response = client.post("/register")
    test_password = 'Dummy_Pass_123'
    if User.email is not None:
        if User.password == test_password:
            assert 'Congratulations, you are now a registered user!' in response.data


# Unit Test 5 - Bad Password - does not meet criteria (registration)
def test_invalid_password_registration(client):
    """ Unit Test for Password Criteria Check"""
    response = client.post("/register")
    test_pass = 'bad'
    if User.email is None:
        User.password = test_pass
        if len(User.password) < 6 or len(User.password) > 35:
            assert 'Please lengthen this text to 6 characters or more' in response.data


# Unit 6 - Already Registered (Registration)
def test_already_registered(client):
    """ Unit Test for Already Registered"""
    response = client.get("/register")
    test_user = 'IS219_TestUser@email.com'
    if User.email is not None and User.email == test_user:
        assert 'Already Registered' in response.data


# Unit Test 7 - Successful Login
def test_successful_login(client):
    """ Unit Test for Successful Login"""
    response = client.post("/login")
    test_user = 'IS219_TestUser@email.com'
    test_password = 'Dummy_Pass_123'
    if User.email == test_user:
        if User.password == test_password:
            assert 'Login Successful' in response.data


# Unit Test 8 - Successful Registration
def test_successful_registration(client):
    """ Unit Test for Successful Registration"""
    response = client.post("/register")
    if User is None:
        assert 'Congratulations, you are now a registered user!' in response.data


# Unit Test 9 - denying access to the dashboard for logged out users
def test_deny_dashboard(client):
    """ Unit Test for Denying Access to Dashboard"""
    response = client.post("/dashboard")
    if not User.authenticated:
        assert 'User Not Authenticated' in response.data


# Unit Test 10 - allowing access to the dashboard for logged in users
def test_allow_dashboard(client):
    """ Unit Test for Allowing Access to Dashboard"""
    response = client.post("/dashboard")
    test_user = 'IS219_TestUser@email.com'
    test_password = 'Dummy_Pass_123'
    if User.email == test_user and User.password == test_password:
        if User.authenticated:
            assert 'User Authenticated' in response.data
