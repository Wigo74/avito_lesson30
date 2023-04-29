import pytest


@pytest.fixture
@pytest.mark.dgango_db
def access_token(client, django_user_model):
    username = "test_user"
    password = "test_passwd"
    django_user_model.objects.create_user(username=username, password=password, role='admin')
    response = client.post("/user/token/", data={"username": username, "password": password}, format='json')
    return response.data.get("access")



@pytest.fixture
@pytest.mark.dgango_db
def user_access_token(client, django_user_model):
    username = "test_user"
    password = "test_passwd"
    test_user = django_user_model.objects.create_user(username=username, password=password, role='admin')
    response = client.post("/user/token/", data={"username": username, "password": password}, format='json')
    return test_user, response.data.get("access")