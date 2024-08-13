import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from user.models import BlogUser

@pytest.mark.django_db
def test_register_user(client, user_data):
    url = reverse('register') 
    response = client.post(url, data=user_data)
    assert response.status_code == 201
    assert BlogUser.objects.filter(username=user_data["username"]).exists()

@pytest.mark.django_db
def test_user_login(client, create_user, user_data):
    url = reverse('login')
    response = client.post(url, data={
        'username': user_data['username'],
        'password': user_data['password']
    })
    assert response.status_code == 302  # Redirect after login
    assert response.url == '/'
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_user_logout(client, create_user, user_data):
    client.login(username=user_data['username'], password=user_data['password'])
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302  # Redirect after logout
    assert not client.session.get('_auth_user_id')

# @pytest.mark.django_db
# def test_user_login_with_wrong_credentials(client, user_data):
#     url = reverse('login')
#     response = client.post(url, data={
#         'username': user_data['username'],
#         'password': 'wrongpassword'
#     })
#     assert response.status_code == 200
#     messages = list(get_messages(response.wsgi_request))
#     assert any("Invalid username or password." in str(message) for message in messages)