import pytest


@pytest.fixture(scope="session")
def pre_setup_work():
    print("I pre-setup browser instance")