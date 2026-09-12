import pytest


@pytest.fixture(scope="session")
def pre_setup_work():
    print("I pre-setup browser instance")
    
@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param